# coding=utf-8

# 发送纯文本
import smtplib
# 发送标题
from email.header import Header
# 邮件正文
from email.mime.text import MIMEText
import random

code = random.sample(list(range(1, 10)), 6)
code = list(map(lambda x: str(x), code))
code = ''.join(code)


# print(sim)
def sendMail(receiver, content, title):
    """
    说明：此函数实现发送邮件功能。
    :param user: 用户名
    :param pwd: 授权码
    :param sender: 发送方
    :param receiver: 接收方
    :param content: 邮件的正文
    :param title: 邮件的标题
    :return:
    """
    mail_user="826746996@qq.com"
    mail_pwd="tpprhkmiewbabcgb"
    sender="826746996@qq.com"
    mail_host = "smtp.qq.com"  # qq的SMTP服务器
    # 第一部分：准备工作
    # 1.将邮件的信息打包成一个对象
    message = MIMEText(content, "plain", "utf-8")  # 内容，格式，编码
    # 2.设置邮件的发送者
    message["From"] = sender
    # 3.设置邮件的接收方
    # message["To"] = receiver
    # join():通过字符串调用，参数为一个列表
    message["To"] = ",".join(receiver)
    # 4.设置邮件的标题
    message["Subject"] = title

    # 第二部分：发送邮件
    try:
        # 1.启用服务器发送邮件
        # 参数：服务器，端口号
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        # 2.登录邮箱进行验证
        # 参数：用户名，授权码
        smtpObj.login(mail_user, mail_pwd)
        # 3.发送邮件
        # 参数：发送方，接收方，邮件信息
        smtpObj.sendmail(mail_user, receiver, message.as_string())
        print("邮件发送成功")
    except:
        print('邮件发送失败')

    # code_1 = input('请输入您收到的验证码：')
    # if code == code_1:
    #     print('恭喜您输入的正确')


if __name__ == "__main__":
    mail_user = "826746996@qq.com"
    mail_pwd = "tpprhkmiewbabcgb"
    mail_sender = "826746996@qq.com"
    shoujian = input('请输入收件人：')
    csr = input('请输入抄送人：')
    receivers = csr.split(' ')
    mail_receiver = receivers + [shoujian]
    email_content = "人生苦短，我用Python." \
                    "您的验证码为：%s" % code
    email_title = "AID人工智能"
    sendMail(mail_receiver, email_content, email_title)
