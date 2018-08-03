# _*_ coding:utf-8 _*_

__author__ = "peiqi"
__date__ = '18-8-3 下午2:18'

from random import Random

from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from mxonline.settings import EMAIL_FROM


def random_str(randomlength = 8):
    str = ''
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0,length)]
    return str


def send_rigister_email(email,send_type = 'register'):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = '死猪佩齐暮雪在线教育注册账号'
        email_body = '点击以下链接激活您的账号：http://127.0.0.1:8000/active/{0}'.format(code)

        send_status = send_mail(email_title,email_body,EMAIL_FROM,[email])
        if send_status:
            pass

    elif send_type == 'forget':
        email_title = '死猪佩齐暮雪在线教育重置密码'
        email_body = '点击以下链接重置您的密码：http://127.0.0.1:8000/reset/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
