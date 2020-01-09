# coding=utf-8

# 发送纯文本
import smtplib
# 发送标题
from email.header import Header
# 邮件正文
from email.mime.text import MIMEText
import random
from mysql01 import Mysql01
from modules import *

# verification_code = random.sample(list(range(1, 10)), 6)
# verification_code = list(map(lambda x: str(x), verification_code))
# verification_code = ''.join(verification_code)


# 判断验证码是否有效

def code_isvaild(email):
    my01=Mysql01()
    # 判断5min内是否有发过验证码
    result=my01.query("select code from vertify_code where email=%s and inittime>(now()-interval 5 minute) order by inittime limit 1",[email])
    if result:
        my01.close()
        return result[0]
    else:
        verification_code = random.sample(list(range(1, 10)), 6)
        verification_code = list(map(lambda x: str(x), verification_code))
        verification_code = ''.join(verification_code)
        my01.in_up_de("insert into vertify_code(email,code)values(%s,%s)",[email,verification_code])
        my01.close()
        return verification_code


#找回密码
def find_screte(email):
    return User_info.query.filter(User_info.email==email).first()

# print(sim)
def sendMail(receiver,title,type):
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
    sender="心欢"
    mail_host = "smtp.qq.com"  # qq的SMTP服务器
    # 第一部分：准备工作
    # 1.将邮件的信息打包成一个对象
    code=None
    if type=="验证码":
        code=code_isvaild(receiver)
        content="您的验证码为%s,有效期为5分钟，请在规定时间内完成验证，如非本人操作，请忽略本邮件"%code
    elif type=="找回密码":
        code=find_screte(receiver)
        content="您的密码为%s，请及时修改密码"%code.pwd
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
        return code
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
                    "您的验证码为：%s" % verification_code
    email_title = "AID人工智能"
    sendMail(mail_receiver, email_content, email_title)
