﻿# Alpha阶段接口说明文档

12.8更新：
“获取用户信息”添加college_id

## 1. 用户相关
### 1.1 记录访问ip
**函数名：** ip_record
**URL：** /sign/iprecord/
**前端**
无需传递参数

**后端**
更新ipvisitinfo表中对应ip的相关字段，若latest_date和当前日期不符，则visit_count自增

变量名|类型|说明
:-:|:-:|:-:
result|int|0:成功（只有一种似乎没太大必要？）

### 1.2 用户注册接口
**函数名：** userRegister
**URL：** /sign/register/
**前端**

变量名|类型|说明
:-:|:-:|:-:
username|str|用户名
password1|str|密码
password2|str|确认密码（无必要）
email|str|电子邮箱，暂定北航
gender|int|性别，男1/女2/保密0
nickname|str|姓名/昵称
intro|str|个人介绍

**后端**
将读到的用户信息存入数据库
变量名|类型|说明
:-:|:-:|:-:
error|int|0:成功<br>201:失败<br>202:异常

### 1.3 获取用户信息
**函数名：** user_information
**URL：** /user/information/
**前端**
以下两种获取方式二选一：

变量名|类型|说明
:-:|:-:|:-:
username|str|用户名或邮箱
id|int|用户id

**后端**

变量名|类型|说明
:-:|:-:|:-:
user_info|dict{}|用户信息

若提供username，用户信息包括：

变量名|类型|说明
:-:|:-:|:-:
username|str|用户名
email|str|邮箱
nickname|str|昵称或姓名
gender|str|性别
intro|str|个人简介
college_id|int|所属院系代号

若提供id，用户信息包括：

变量名|类型|说明
:-:|:-:|:-:
username|str|用户名
email|str|邮箱

### 1.4 判断用户是否登录
**函数名：** get_user
**URL：** /sign/get_user/
**前端**
无需传递参数

**后端**

变量名|类型|说明
:-:|:-:|:-:
is_login|bool|登录为true，否则为false

### 1.5 用户登录
**函数名：** userLogin
**URL：** /sign/login/
**前端**

变量名|类型|说明
:-:|:-:|:-:
username|str|用户名
password|str|密码

**后端**
若成功登录，则修改session：
变量名|类型|说明
:-:|:-:|:-:
username|str|当前登录的用户名

返回

变量名|类型|说明
:-:|:-:|:-:
error|int|0:成功<br>101:失败<br>102:异常

### 1.6 用户登出
**函数名：** userLogout
**URL：** /sign/logout/
**前端**
无需传递参数

**后端**

变量名|类型|说明
:-:|:-:|:-:
error|int|0:成功<br>301:失败




## 2. 课程相关
### 2.1 获取某学院下课程信息列表
**函数名：** course\_by\_college
**URL：** /course/college_course/
**前端**

变量名|类型|说明
:-:|:-:|:-:
college_id|int|学院的id

**后端**

变量名|类型|说明
:-:|:-:|:-:
course\_info\_list|list[info{}]|一个由课程信息组成的列表，课程信息是个字典，包含数据库课程表的所有字段

### 2.2 获取某类型下课程信息列表
**函数名：** course\_by\_class
**URL：** /course/class_course/
**前端**

变量名|类型|说明
:-:|:-:|:-:
class_id|int|类别的id

**后端**

变量名|类型|说明
:-:|:-:|:-:
course\_info\_list|list[info{}]|一个由课程信息组成的列表，课程信息是个字典，包含数据库课程表的所有字段

### 2.3 获取课程信息
**函数名：** course_information
**URL：** /course/course_info/ （想修改为information）
**前端**

变量名|类型|说明
:-:|:-:|:-:
course_id|int|课程的id

**后端**
变量名|类型|说明
:-:|:-:|:-:
course_info|dict{}|包含数据库课程表的所有字段

### 2.4 更新课程访问数量
**函数名：** refresh_visit_course_count
**URL：** /course/visit_count/
**前端**

变量名|类型|说明
:-:|:-:|:-:
course_id|int|课程id

**后端**
除非上一次访问时间在24小时内，否则修改课程表中该course对应记录的visit_count字段，使其自增1，并进行session存储：

变量名|类型|说明
:-:|:-:|:-:
last\_view[course\_id]|dict{str:str}|course\_id转成str类型作为键，值为当前的datetime转成str类型

传回数据：
变量名|类型|说明
:-:|:-:|:-:
visit_count|int|当前访问量

### 2.5 搜索课程
**函数名：** course_query
**URL：** /course/searching/
**前端**

变量名|类型|说明
:-:|:-:|:-:
keyword|str|搜索关键词

**后端**

变量名|类型|说明
:-:|:-:|:-:
query_list|list[dict{}]|一个由课程信息组成的列表，课程信息是个字典，包含数据库课程表的所有字段

### 2.6 获取课程最新课件信息列表
**函数名：** latest_resource_info
**URL：** /resource/latest/
**前端**

变量名|类型|说明
:-:|:-:|:-:
course_id|int|课程id
number|int|资源数量

**后端**

变量名|类型|说明
:-:|:-:|:-:
result|list[dict{}]|返回资源信息列表

资源信息字典：

变量名|类型|说明
:-:|:-:|:-:
resource_id|int|资源id
username|str|上传者
download_count|int|下载量
name|str|资源名称




## 3. 资源相关
### 3.1 更新资源下载数量
**函数名：** refresh_download_resource_count
**URL：** /resource/download_count/
**前端**

变量名|类型|说明
:-:|:-:|:-:
download\_count|int|资源id

**后端**
除非上一次下载时间在24小时内，否则修改课程表中该course对应记录的download_count字段，使其自增1，并进行session存储：

变量名|类型|说明
:-:|:-:|:-:
last\_download[resource\_id]|dict{str:str}|resource\_id转成str类型作为键，值为当前的datetime转成str类型

传回数据：
变量名|类型|说明
:-:|:-:|:-:
download\_count|int|当前访问量

### 3.2 获取资源信息
**函数名：** resource_information
**URL：** /resource/information/

**前端**

变量名|类型|说明
:-:|:-:|:-:
resource_id|int|资源id

**后端**
变量名|类型|说明
:-:|:-:|:-:
resource_info|dict{}|资源信息，包含数据库课程表的所有字段

### 3.3 获取课程资源列表
**函数名：** resource\_id\_list
**URL：** /resource/id/list/
**前端**

变量名|类型|说明
:-:|:-:|:-:
course_id|int|课程id

**后端**

变量名|类型|说明
:-:|:-:|:-:
resource\_id\_list|list[int]|该课程下的资源id列表

### 3.4 资源上传
**函数名：** resourceUpload
**URL：** /resourceUpload/
**前端**

变量名|类型|说明
:-:|:-:|:-:
intro|int|资源简介
course_code|int|课程代码
only_url|str|是否为引用的其他地方的资源（感觉用bool会更好）
url|str|下载链接，需要only_url为True
name|name|资源名字，需要only_url为True

**后端**
将资源信息储存到Resource表中

变量名|类型|说明
:-:|:-:|:-:
error|int|0:成功<br>1:失败

### 3.5 资源下载
**函数名：** download
**URL：** /download/
**前端**
无需传递参数

**后端**
传回文件或下载链接

## 4. 其它
### 4.1 作用不明
isLoggedIn

### 4.2 未使用
user_info_modify
user_report
handle_upload_resource
get_username
course_contrib_list