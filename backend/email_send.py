'''
Created on 2017年12月8日

@author: 15061188
'''
from random import Random # 用于生成随机码 
from django.core.mail import send_mail # 发送邮件模块
from backend.models import EmailVerifyRecord # 邮箱验证model
from iCourse.settings import EMAIL_FROM  # setting.py添加的的配置信息


# 生成随机字符串
def random_str(randomlength=8):
    _str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        _str+=chars[random.randint(0, length)]
    return _str


def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    
    # 将给用户发的信息保存在数据库中
    code = random_str(16)
    
    email_record.code = code
    print(code)
    email_record.email = email
    print(email)
    email_record.send_type = send_type
    print(send_type)
    email_record.save()
    # 初始化为空
    email_title = ""
    email_body = ""
    # 如果为注册类型
    if send_type == "register":
        email_title = "icourse账号注册激活链接"
        email_body = "您好，我们是icourse课程平台开发团队，请点击链接激活你的账号:http://buaaicourse.com/active/{0}".format(code)
        # 发送邮件
        
        print(email_title)
        print(email_body)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass