#iCourse课程平台测试报告

本报告由“烫烫烫烫烫”团队撰写

##测试环境及工具

 - windows10/selenium/jmeter/badboy/firefox/chrome/IE
 - 本着尽可能使用自动化测试的原则，又考虑到测试人员对java更为熟悉，因此功能测试使用java版本的selenium，首先由firefox的selenium IDE插件录制测试用例，导出为java/Junit4/webdriver格式的代码，手动修改部分代码使之能够正常运行，回归测试时只需重新运行即可。
 - 负载测试采用jmeter和badboy实现，首先由badboy录制测试用例，导出为jmx格式，jmeter可直接使用，通过设置jmeter运行时的线程数，发送请求等参数控制网站负载，完成负载测试和压力测试。

##测试用例

 - 测试注册功能：TestRegister.java
 - 测试用户登录和访问个人中心：TestLoginAndUserInfo.java

##错误报告

 - 2017.11.07 版本号：931275f

		环境：本地运行python manage.py runserver,运行成功。

		(未解决)bug1:打开firefox，登陆127.0.0.1:8000/course,搜索栏内输入“软件工程”，按回车，报错如下：
![nameError](https://i.imgur.com/u2ho7B2.jpg)
		
		分析：输入其他字符，按回车，也会报上面的错，估计是缺少对回车的支持

##优化建议：

 - 2017.11.07 版本号：931275f

		环境：本地运行python manage.py runserver,运行成功。

		(未解决)优化建议:打开firefox，登陆127.0.0.1:8000/course,
		[1]搜索栏内输入“软件工程”，点击“搜索”，会弹出对话框“成功！开始搜索”，
		[2]点击具体的课程类别和具体的系号，会弹出对话框“success”。
		从测试角度看，保留这两个可以理解~从用户角度看，最好上线前把这个删掉~记录一下，防止遗忘。