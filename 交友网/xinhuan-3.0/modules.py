from flask import Flask
#导入sqlalchemy
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
import datetime

# 将当前的模块构建成flask应用
# 当flask应用构建完成后就可以接受请求并给出响应
app = Flask(__name__)
# app.config.from_object(config)#加盐

app.config["SQLALCHEMY_DATABASE_URI"]="mysql://exchange:321@127.0.0.1:3306/soul"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True

#创建sqlalchemy 实例
db=SQLAlchemy(app)
#db 表示正在使用的数据库,同时获得了sqlslchemy的所有功能

class User_info(db.Model):
    __tablename__="user_info"
    uid=db.Column(db.Integer,primary_key=True)    
    username=db.Column(db.String(20))
    pwd=db.Column(db.String(50))
    user_type=db.Column(db.String(2))
    tel=db.Column(db.String(11))
    email=db.Column(db.String(50))
    address=db.Column(db.String(20))
    graph=db.Column(db.Binary(200)) 
    sex=db.Column(db.String(2))   
    def __init__(self,uid=None,sex="",username="",pwd="",user_type="0",tel="",address="",graph="",email=""):
        self.uid=uid
        self.username=username
        self.pwd=pwd
        self.user_type=user_type
        self.tel=tel
        self.address=address
        self.graph=graph
        self.email=email
        self.sex=sex


class User_loginlogs(db.Model):
    __tablename__="user_loginlogs"
    id=db.Column(db.Integer,primary_key=True)
    loguid=db.Column(db.String(30))
    login_time=db.Column(db.DateTime)
    logout_time=db.Column(db.DateTime)
    def __init__(self,loguid,login_time,logout_time):
        self.loguid=loguid
        self.login_time=login_time
        self.logout_time=logout_time

class Vertify_code(db.Model):
    __tablename__="vertify_code"
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(50))
    code=db.Column(db.String(30)) 
    inittime=db.Column(db.DateTime,default=datetime.datetime.now())
    def __init__(self,email,code):
        self.email=email
        self.code=code        

class User_life_circle(db.Model):
    __tablename__="user_life_circle"
    id=db.Column(db.Integer,primary_key=True)
    uid=db.Column(db.String(20))
    content=db.Column(db.String(2000))
    posted_time=db.Column(db.DateTime)
    def __init__(self,uid,content):
        self.uid=uid
        self.content=content

class User_circle_comment(db.Model):
    __tablename__="user_circle_comment"
    id=db.Column(db.Integer,primary_key=True)
    uid=db.Column(db.String(10))
    circle_id=db.Column(db.String(10))
    comment=db.Column(db.String(500))
    kiss=db.Column(db.Integer)
    inittime=db.Column(db.DateTime)
    def __init__(self,uid,circle_id,comment,kiss):
        self.uid=uid
        self.circle_id=circle_id
        self.comment=comment
        self.kiss=kiss

class User_sign_in(db.Model):
    __tablename__="user_sign_in"
    id=db.Column(db.Integer,primary_key=True)
    uid=db.Column(db.String(10))
    kiss_count=db.Column(db.Integer)
    kiss_day=db.Column(db.Date)
    def __init__(self,uid,kiss_count,kiss_day):
        self.uid=uid
        self.kiss_count=kiss_count
        self.kiss_day=kiss_day
    



