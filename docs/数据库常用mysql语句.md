

## 视图

R: `create view R as select * from backend_resource;`

U: `create view U as select * from auth_user;`

C: `create view C as select * from backend_course;`

UP: `create view UP as select * from backend_userprofile;`

这样之后的操作可以简便，例如查看用户信息的列信息，可以直接：`show columns from UP;`


#### 查询下载次数前100的资源

```
select name,download_count from R order by download_count desc limit 100;
```


#### 统计资源个数最多的50个资源

```
select course_code, count(*) from R group by course_code order by count(*) desc limit 50;
```

#### 部分匹配查询资源或课程


```
select * from C where name like '%数据库%';
```

#### 按照递增顺序显示已经注册的用户有哪些院系

```
select distinct college_id from UP order by college_id asc;
```

#### 查看用户的用户名，邮箱，性别，学院


一个简单的连表操作（因为信息分布在auth_user和backend_userprofile里）

```
select username, email, gender, college_id from U,UP where UP.user_id = U.id;
```

####  查询某个相关课程的所有资源

嵌套查询。

```
select name from R where course_code = any (select course_code from C where name like '%数据库%');
```

注:
=any 可以直接用 in 来替代



#### 查询有人评分过的资源

可以用表的连接

```
select name from R, backend_resource_evaluation where R.id = backend_resource_evaluation.resource_id;
```

或者嵌套子表用exist

```
select name from R where exists (select * from backend_resource_evaluation where resource_id = R.id);
```


