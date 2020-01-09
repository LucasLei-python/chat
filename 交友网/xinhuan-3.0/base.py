
from modules import *
import datetime

def email_exist(email):
    """
        验证邮箱地址是否存在
    """
    try:
        result=User_info.query.filter(User_info.email==email).first()
        if result:            
            return result
    except Exception as e:
        return "Error："+str(e)

def login_check(email,pwd):
    """
        登录验证
    """
    try:
        result=User_info.query.filter(User_info.email==email,User_info.pwd==pwd).first()
        if result is None:
            return "Error:账号密码错误，请确认"
        else:
            return result
    except Exception as e:
        return "Error："+str(e)

def write_logs(uid):
    """
        写入登录日志
    """
    try:
        db.session.add(User_loginlogs(uid,datetime.datetime.now(),None))       
    except Exception as e:
        return "Error："+str(e)

def check_code(email,vercode):
    """
        验证验证码是否过期或正确
    """
    try:       
        query=Vertify_code.query.filter(Vertify_code.email==email,Vertify_code.code==vercode,Vertify_code.inittime>=(datetime.datetime.now()-datetime.timedelta(minutes=250))).order_by(Vertify_code.inittime.desc()).first()
        if not query:
            return "Error:验证码不存在或已过期，请重新获取" 
    except Exception as e:
        return "Error："+str(e)

def insert_user_info(username,pwd,email):
    try:
        db.session.add(User_info(username=username,pwd=pwd,email=email))     
    except Exception as e:
        return "Error："+str(e)
    
    
