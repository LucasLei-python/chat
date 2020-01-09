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
    def __init__(self,uid=None,sex=None,username=None,pwd=None,user_type="0",tel=None,address=None,graph=None,email=None):
        self.uid=uid
        self.username=username
        self.pwd=pwd
        self.user_type=user_type
        self.tel=tel
        self.address=address
        self.graph=graph
        self.email=email

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

# db.create_all()
# @app.route('/')
# def test():
#     result=db.session.query(User_info).first()
#     # db.session.add(User_info('dd','dd'))
    
#     print(result.id,result.loguid)
#     return "Hello world"


# if __name__ == "__main__":
#     app.run(debug=False,port=5001)

