# Beta阶段接口说明文档
## 1. 用户相关
### 1.1 修改认证邮箱-提出修改申请
**函数名：** user\_modify\_email\_send
**URL：** /user/modify/email/send
**前端**
变量名|类型|说明
:-:|:-:|:-:
user_id|int|用户id
email|str|新邮箱
password|str|密码

**后端**
如果密码正确，需要向邮箱里发送随机的验证密码，在数据库中存储发送的时间（当前时间）、发送的验证密码和新的邮箱（不覆盖旧邮箱），可能涉及对数据库表结构的修改，再议
变量名|类型|说明
:-:|:-:|:-:
error|int|0:成功发送验证消息<br>1:发送失败<br>2:发送过于频繁<br>3:密码错误<br>4:未知错误

### 1.2 修改认证邮箱-完成修改
**函数名：** user_modify_email
**URL：** /user/modify/email
**前端**
变量名|类型|说明
:-:|:-:|:-:
user_id|int|用户id
code|str|发送到邮箱的验证密码

**后端**
如果验证密码匹配，将新邮箱覆盖到旧邮箱，同时清除user\_modify\_email\_send中对数据库的修改

变量名|类型|说明
:-:|:-:|:-:
error|int|0:成功<br>1:验证密码不匹配<br>2:验证超时<br>3:未知错误

### 1.3 修改个人信息
**函数名：** user\_modify\_info
**URL：** /user/modify/info
**前端**
变量名|类型|说明
:-:|:-:|:-:
nikename|str|昵称或姓名
gender|str|性别，'1'男，'2'女，'0'保密
intro|str|个人简介
college_id|int|院系id

**后端**
变量名|类型|说明
:-:|:-:|:-:
error|int|0:成功<br>1:失败

### 1.4 修改密码
**函数名：** user\_modify\_password
**URL：** /user/modify/password/
**前端**
变量名|类型|说明
:-:|:-:|:-:
user_id|int|用户id
old_pw|str|旧密码
new_pw|str|新密码

**后端**
若旧密码匹配，将新密码覆盖到旧密码上

变量名|类型|说明
:-:|:-:|:-:
error|int|0:成功<br>1:旧密码错误<br>2:未知错误

### 1.5 忘记密码-提交申请
**函数名：** user\_forget\_password\_send
**URL：** /user/forgot/password/send/
**前端**
变量名|类型|说明
:-:|:-:|:-:
user_id|int|用户id

**后端**
需要向邮箱里发送随机的验证密码，在数据库中存储发送的时间（当前时间）和发送的验证密码，可能涉及对数据库表结构的修改，再议
变量名|类型|说明
:-:|:-:|:-:
error|int|0:成功<br>1:发送失败<br>2:申请过于频繁<br>3:未知错误

### 1.6 忘记密码-设置密码
**函数名：** user\_forget\_password\_set
**URL：** /user/forget/password/set/
**前端**
变量名|类型|说明
:-:|:-:|:-:
user_id|int|用户id
code|str|验证密码
new_pw|str|新密码

**后端**
变量名|类型|说明
:-:|:-:|:-:
error|int|0:成功<br>1:验证密码不匹配<br>2:验证超时<br>3:未知错误

## 2. 课程相关
### 2.1 保存搜索记录
**函数名：** add\_history\_keywords
**URL：** /course/searching/history/add/
**前端**
变量名|类型|说明
:-:|:-:|:-:
keyword|str|搜索关键词

**后端**
修改session，将keyword加入到list中：
变量名|类型|说明
:-:|:-:|:-:
keyword_list|list[str]|历史搜索关键词列表，长度上限为10

返回
变量名|类型|说明
:-:|:-:|:-:
error|int|0:成功<br>1:失败

### 2.2 获取搜索记录
**函数名：** get\_history\_keywords
**URL：** /course/searching/history/get/
**前端**
前端无需提供数据

**后端**
读取session：
变量名|类型|说明
:-:|:-:|:-:
keyword_list|list[str]|历史搜索关键词列表，长度上限为10

返回
变量名|类型|说明
:-:|:-:|:-:
keyword_list|list[str]|历史搜索关键词列表，长度上限为10

### 2.3 清除搜索记录
**函数名：** clean\_history\_keywords
**URL：** /course/searching/history/clean/
**前端**
前端无需提供数据

**后端**
修改session，清空列表：
变量名|类型|说明
:-:|:-:|:-:
keyword_list|list[str]|历史搜索关键词列表，长度上限为10

返回
变量名|类型|说明
:-:|:-:|:-:
error|int|0:成功<br>1:失败

### 2.4 获取历史访问课程id列表
**函数名：** get\_history\_courses\_id
**URL：** /course/list/history/
**前端**
前端无需提供数据

**后端**
读取session：
变量名|类型|说明
:-:|:-:|:-:
history\_course\_idlist|list[int]|历史访问课程id列表，长度上限为10

返回
变量名|类型|说明
:-:|:-:|:-:
history\_course\_idlist|list[int]|历史访问课程id列表，长度上限为10
history\_course\_namelist|list[str]|历史访问课程名称列表，长度上限为10，两个列表元素位置对应

### 2.5 获取最热访问课程id列表
**函数名：** get\_hot\_courses\_id
**URL：** /course/list/hot/
**前端**
前端无需提供数据

**后端**
变量名|类型|说明
:-:|:-:|:-:
hot\_course\_idlist|list[int]|热门访问课程id列表，长度上限为10
hot\_course\_namelist|list[str]|热门访问课程名称列表，长度上限为10，两个列表元素位置对应

### 2.6 获取收藏课程id列表
**函数名：** get\_like\_courses\_id
**URL：** /course/list/like/
**前端**
变量名|类型|说明
:-:|:-:|:-:
user_id|int|用户id

**后端**
变量名|类型|说明
:-:|:-:|:-:
like\_course\_idlist|list[int]|用户收藏课程id列表，长度上限为10
like\_course\_namelist|list[str]|用户收藏课程名称列表，长度上限为10，两个列表元素位置对应

### 2.7 获取课程最热课件信息列表
**函数名：** hot\_resource\_info
**URL：** /resource/hot/
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

### 2.8 课程收藏
**函数名：** course\_like
**URL：** /course/like/add/
**前端**
变量名|类型|说明
:-:|:-:|:-:
course_id|int|课程id
user_id|int|用户id

**后端**
变量名|类型|说明
:-:|:-:|:-:
error|int|0:成功<br>1:失败

### 2.9 课程取消收藏
**函数名：** course\_cancel\_like
**URL：** /course/like/cancel/
**前端**
变量名|类型|说明
:-:|:-:|:-:
course_id|int|课程id
user_id|int|用户id

**后端**
变量名|类型|说明
:-:|:-:|:-:
error|int|0:成功<br>1:失败

### 2.10 获取课程收藏情况
**函数名：** course\_like\_count
**URL：** /course/like/count/
**前端**
变量名|类型|说明
:-:|:-:|:-:
course_id|int|课程id
user_id|int|用户id

**后端**
变量名|类型|说明
:-:|:-:|:-:
like_count|int|收藏数
liked|int|0:未收藏<br>1:已收藏


### 课程简介修改

## 3. 资源相关
### 3.1 获取某一类别资源（修改）
**函数名：** resource\_id\_list
**URL：** /resource/id/list/
**前端**

变量名|类型|说明
:-:|:-:|:-:
course_id|int|课程id
type|int|资源类别: ppt、doc(txt)、pdf、pict、other、all

**后端**

变量名|类型|说明
:-:|:-:|:-:
resource\_id\_list|list[int]|该课程下的资源id列表

### 3.2 搜索资源
**函数名：** resource_query
**URL：** /resource/searching/
**前端**

变量名|类型|说明
:-:|:-:|:-:
keyword|str|搜索关键词
course_id|int|课程id，-1表示全局搜索
type|str|资源类别: ppt、doc(txt)、pdf、pict、other、all

**后端**
变量名|类型|说明
:-:|:-:|:-:
query_list|list[int]|一个由资源id组成的列表，课程信息是个字典，包含数据库课程表的所有字段

### 3.3 资源收藏
**函数名：** resource\_like
**URL：** /resource/like/add/
**前端**
变量名|类型|说明
:-:|:-:|:-:
resource_id|int|资源id
user_id|int|用户id

**后端**
变量名|类型|说明
:-:|:-:|:-:
error|int|0:成功<br>1:失败

### 3.4 资源取消收藏
**函数名：** resource\_cancel\_like
**URL：** /resource/like/cancel/
**前端**
变量名|类型|说明
:-:|:-:|:-:
resource_id|int|资源id
user_id|int|用户id

**后端**
变量名|类型|说明
:-:|:-:|:-:
error|int|0:成功<br>1:失败

### 3.5 获取资源收藏情况
**函数名：** resource\_like\_count
**URL：** /resource/like/count/
**前端**
变量名|类型|说明
:-:|:-:|:-:
resource_id|int|资源id
user_id|int|用户id

**后端**
变量名|类型|说明
:-:|:-:|:-:
like_resource|int|收藏数
like|int|0:未收藏<br>1:已收藏

### 3.6 资源评价
**函数名：** resource_evaluate
**URL：** /resource/evaluate/
**前端**
变量名|类型|说明
:-:|:-:|:-:
resource_id|int|资源id
user_id|int|用户id
| grade   | int |评分，0~5

**后端**
变量名|类型|说明
:-:|:-:|:-:
error|int|0:成功<br>1:失败

### 3.7 获取资源评价情况
**函数名：** resource\_evaluation\_grade\_count
**URL：** /resource/evaluation/grade/count/
**前端**
变量名|类型|说明
:-:|:-:|:-:
resource_id|int|资源id
user_id|int|用户id

**后端**
变量名|类型|说明
:-:|:-:|:-:
avg_grade|int|评价平均分
user_grade|int|用户给予的评价，未评价返回-1

### 3.8 获取评论id列表（暂废）
**函数名：** resource\_evaluation\_comment\_idlist
**URL：** /resource/evaluation/comment/idlist/
**前端**
变量名|类型|说明
:-:|:-:|:-:
resoruce_id|int|资源id

**后端**
变量名|类型|说明
:-:|:-:|:-:
idlist|list[int]|包含所有评论（必须写了文字的）id的列表

### 3.9 获取评论内容（暂废）
**函数名：** resource\_evaluation\_comment\_content
**URL：** /resource/evaluation/comment/content/
**前端**
变量名|类型|说明
:-:|:-:|:-:
idlist|list[int]|评论id列表

**后端**
变量名|类型|说明
:-:|:-:|:-:
content_list|list[dict{}]|内容列表

字典包括：
变量名|类型|说明
:-:|:-:|:-:
comment|str（longtext？）|评论文字，不能为null
grade|int|0:未进行好评/差评<br>1:好评<br>-1:差评
user_id|int|评价者id
username|str|评价者用户名
time|datetime|发布时间


### 资源简介修改
**函数名：** 
**URL：** /
**前端**
变量名|类型|说明
:-:|:-:|:-:

**后端**
变量名|类型|说明
:-:|:-:|:-:

## 4. 消息
### 举报
### 审核

## 5. 博文
### 发表博文
**函数名：** posting_publish
**URL：** /post/posting/publish/
**前端**
变量名|类型|说明
:-:|:-:|:-:
title|str|标题
course_id|int|课程id
category|int|分类码，如1表提问、2表文章、0表其它等
content|longtext|内容
user_id|int|发表人id
post_time|datetime|发布时间
editor|int|编辑器代码，0=quill,1=markdown


**后端**
变量名|类型|说明
:-:|:-:|:-:
error|int|0:成功<br>1:失败

### 跟帖
**函数名：** follow_publish
**URL：** /post/follow/publish/
**前端**
变量名|类型|说明
:-:|:-:|:-:
post_id|int|帖子id
content|longtext|内容
user_id|int|发表人id
post_time|datetime|发布时间
editor|int|编辑器代码，0=quill,1=markdown
published|bool|是否已经发布

**后端**
变量名|类型|说明
:-:|:-:|:-:
error|int|0:成功<br>1:失败

### 评论
**函数名：** comment_publish
**URL：** /post/comment/publish/
**前端**
变量名|类型|说明
:-:|:-:|:-:
user\_id|int|发表人id
follow_id|int|所属跟帖id
to\_comment\_id|int|要回复的评论id，没有填-1
content|textfield|评论内容
post\_time|datetime|发表时间

**后端**
变量名|类型|说明
:-:|:-:|:-:
error|int|0:成功<br>1:失败

### 赞同/反对
**函数名：** follow_evaluate
**URL：** /post/follow/evaluate
**前端**
变量名|类型|说明
:-:|:-:|:-:
user_id|int|评价人id
follow_id|int|跟帖id
grade|int|评价，1表赞同，-1表反对

**后端**
变量名|类型|说明
:-:|:-:|:-:
error|int|0:成功<br>1:失败

### 获取课程讨论版帖子id列表
**函数名：** post\_id\_list
**URL：** /post/id/list/
**前端**
变量名|类型|说明
:-:|:-:|:-:
course_id|int|课程id

**后端**
变量名|类型|说明
:-:|:-:|:-:
id_list|list[int]|该课程下所有帖子的id列表，按照更新时间排序

### 获取帖子信息列表（评价情况、跟帖数、*顶楼部分内容）
**函数名：** post\_infor\_list
**URL：** /post/information/list/
**前端**
变量名|类型|说明
:-:|:-:|:-:
id_list|list[int]|该课程下所有帖子的id列表
get_content|bool|是否获取顶楼内容
get_grade|bool|是否获取赞同情况
get\_follow\_count|是否获取跟帖数

**后端**
变量名|类型|说明
:-:|:-:|:-:
info_list|list[dict{}]|信息列表

字典包括：
变量名|类型|说明
:-:|:-:|:-:
title|str|标题
category|int|分类码
user_id|int|用户id
username|int|上传者用户名（冗余）
read_count|int|阅读数
update_time|datetime|更新时间
content|textfield|顶楼内容（纯文本）
grade_sum|int|所有跟帖的赞同数总和
follow_count|int|跟帖数（顶楼不算在内）

### 获取跟帖id列表
**函数名：** follow\_id\_list
**URL：** /follow/id/list/
**前端**
变量名|类型|说明
:-:|:-:|:-:
post_id|int|帖子id

**后端**
变量名|类型|说明
:-:|:-:|:-:
main_id|int|主楼id
id\_list|list[int]|非主楼id列表，按照（赞同数-反对数）排序


### 获取跟帖信息列表（内容、评价情况、是否为发布人等）
**函数名：** follow\_info\_list
**URL：** /follow/info/list/
**前端**
变量名|类型|说明
:-:|:-:|:-:
id_list|list[int]|跟帖id列表
cur\_user\_id|int|浏览者id，未登录为-1

**后端**
变量名|类型|说明
:-:|:-:|:-:
info_list|list[dict{}]|信息列表

字典包括：
变量名|类型|说明
:-:|:-:|:-:
user_id|int|用户id
username|str|用户名
is_poster|bool|浏览者是否为发布者，未登录为false
evaluated_grade|int|评价情况，1赞同，-1反对，未登录与未评价为0
post_time|datetime|发布时间
edit_time|datetime|编辑时间
content|textfield|内容

### 获取用户跟帖
**函数名：** 
**URL：** /
**前端**
变量名|类型|说明
:-:|:-:|:-:
post_id|int|帖子id
user_id|int|用户id

**后端**
变量名|类型|说明
:-:|:-:|:-:
content|textfield|内容
editor|int|编辑器编号

### 获取评论信息列表


**函数名：** 
**URL：** /
**前端**
变量名|类型|说明
:-:|:-:|:-:

**后端**
变量名|类型|说明
:-:|:-:|:-:

