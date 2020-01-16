# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 15:19
# @Author  : hero1210
# @Site    : 
# @File    : send_message.py
# @Software: PyCharm


import zhenzismsclient as smsclient

# 生成随机验证码
import random


code = ""
for num in range(0, 6):
    code = code + str(random.randint(0, 9))


# 参数
# apiUrl为请求地址

apiUrl = "http://sms_developer.zhenzikj.com"
appId = "101546"
appSecret = "YzNmY2MyNGItYzQ5ZS00ZmQ0LWJhMTEtNjEyYTY3MWZjZDky"

# 初始化ZhenziSmsClient
client = smsclient.ZhenziSmsClient(apiUrl, appId, appSecret)

phone_num = input("请输入接受信息的手机号：")

msg = "%s，您的验证码是%s，5分钟内有效，请注意保密。" % (phone_num, code)
result = client.send(phone_num, msg)
print(result)

