# iCourse
Software Engineering, BUAA 课程资源共享平台

---

## 1. 必要的安装
安装python3：https://www.python.org/downloads/（开发所用的版本为3.6.1）

Node.js和npm的安装：https://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000/00143450141843488beddae2a1044cab5acb5125baf0882000
由于某种原因，国内对npm的使用可能受到影响，可以使用淘宝提供的npm镜像，以cnpm代替npm：https://npm.taobao.org/

安装django：

    pip install django

## 2. 部署之前
进入/frontend/目录下，执行命令

    cnpm install

上述命令的作用是安装前端所需的必要插件。

此外运行后可能会提示缺少必要的python包等情况，需要使用pip进行安装。

## 3. 简单部署
### 3.1 本地
在主目录下执行命令：

    py -3 manage.py runserver
    
### 3.2 服务器
在主目录下执行命令：

    py -3 manage.py runserver 0.0.0.0:8000
    
## 4. 使用Nginx + uWSGI + Supervisor配置服务器（Ubuntu）
### 4.1 配置uWSGI
安装uWSGI：

    pip install uwsgi
    uwsgi --version    # 查看 uwsgi 版本

在/ect/目录下新建uwsgi.ini，添加如下配置：

    [uwsgi]
    socket = 127.0.0.1:8001         # 和conf文件中的server保持一致
    chdir = /home/icourse/iCourse   # 项目位置
    wsgi-file = iCourse/wsgi.py     # wsgi.py位置（相对chdir）
    master = true
    processes = 4
    #threads = 2
    #module = iCourse.wsgi
    vacuum = true                   # 清除文件
    buffer-size = 30000

### 4.2 配置Nginx
安装Nginx：

    cd ~
    wget http://nginx.org/download/nginx-1.5.6.tar.gz
    tar xf nginx-1.5.6.tar.gz
    cd nginx-1.5.6
    ./configure --prefix=/usr/local/nginx-1.5.6 \
    --with-http_stub_status_module \
    --with-http_gzip_static_module
    make && make install

找到nginx的安装目录（如：/usr/local/nginx/），打开conf/nginx.conf文件，修改server配置：

    upstream django {
            server 127.0.0.1:8001;
    }
    server {
            listen       8000;
            server_name  origin_icourse;
            location /static {
                alias /home/icourse/iCourse/frontend/dist/static;
            }
            location / {
                include  uwsgi_params;
                uwsgi_pass  django;
                include /etc/nginx/uwsgi_params;
                uwsgi_param UWSGI_SCRIPT iCourse.wsgi;
                uwsgi_param UWSGI_CHDIR /iCourse;
                index  index.html index.htm;
                client_max_body_size 35m;
            }
    }

    
### 4.3 配置Supervisor
安装Supervisor：

    pip install supervisor
    
生成配置文件：

    echo_supervisord_conf > /etc/supervisord.conf
    
编辑/etc/supervisord.conf，在最后加上：

    [program:iCourse]
    command=/usr/local/bin/uwsgi --ini /home/icourse/uwsgi8000.ini
    directory=/home/icourse/iCourse
    startsecs=0
    stopwaitsecs=0
    autostart=true
    autorestart=true

### 4.4 运行/重启/结束
运行：

    $ sudo supervisorctl start iCourse 

重启（在每次对代码进行变动后都要重启项目）：

    $ sudo supervisorctl restart iCourse 

结束

    $ sudo supervisorctl stop iCourse 
