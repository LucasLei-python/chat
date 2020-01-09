#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, render_template,session,url_for
from flask import request, make_response,jsonify,redirect,flash
from mysql01 import Mysql01
from sendemail import *
import config
from Islogin import need_login
import time,datetime
from modules import *
import base
#导入sqlalchemy
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
import json

# 导入日志模块
# from rizhi import logging

# from forms import NewPostForm

# 将当前的模块构建成flask应用
# 当flask应用构建完成后就可以接受请求并给出响应
# app = Flask(__name__)

app.config.from_object(config)#加盐

my01 = Mysql01()


# 首页
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=="GET":
        return render_template("index.html")
    else:
        return ""

# 登录页面
@app.route('/user/login', methods=['GET', 'POST'])
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        data=json.loads(request.get_data(as_text=True), strict=False)
        email=data.get("email")
        pwd=data.get("pass")
        dict_msg={}
        result=base.login_check(email,pwd)       
        if type(result) is str:                 
            dict_msg={"status":"1002","Msg":result,"value":""}
        else:
            session["email"]=email
            session["username"]=result.username
            if not base.write_logs(result.uid):
                dict_msg={"status":"1000","Msg":"登录成功","value":"/"}
            else:
                dict_msg={"status":"1001","Msg":"登录失败","value":""}
        return jsonify(dict_msg)
# 注册页面
@app.route('/user/reg', methods=['GET', 'POST'])
def reg():
    if request.method=="GET":
        return render_template("reg.html")
    else:        
        data=request.get_json()        
        # data = json.loads(request.get_data(as_text=True), strict=False)
        ''' 
            data = json.loads(request.get_data(as_text=True), strict=False)
            data=request.get_json()
            data=request.json 
            都可以实现接受json数据，但是后两种需要在请求时要设置请求头xhr.setRequestHeader('Content-Type',"application/json");
            loads()是把json格式去掉''(the JSON object must be str, bytes or bytearray, not 'dict')
        '''        
        sub_type=data.get("type")        
        email=data.get("email")
        dict_msg={}
        # 判断邮箱是否存在  
        is_exist=base.email_exist(email)
        if is_exist: 
            if not type(is_exist) is str:
                dict_msg={"status":"1002","Msg":"该邮箱已经注册,不能重复注册","value":""}  
            else:#try出来的错误信息
                dict_msg={"status":"1002","Msg":is_exist,"value":""}        
        elif sub_type=="发送验证码":
            validcode=sendMail(email,'【❤H】验证码：','验证码')
            if  validcode:
                dict_msg={"status":"1000","Msg":"邮件发送成功","value":""}
            else:
                dict_msg={"status":"1001","Msg":"邮件发送失败","value":""}
        elif sub_type=="注册提交":
            # 判断验证码是否正确
            vercode=data.get("vercode")
            result=base.check_code(email,vercode)
            if result:
                dict_msg={"status":"1001","Msg":result,"value":""}
            # 写入数据
            else:
                result=base.insert_user_info(data.get("username"),data.get("pass"),data.get("email"))
                if result:
                    dict_msg={"status":"1002","Msg":result,"value":""}
                else:
                    dict_msg={"status":"1000","Msg":"注册成功","value":"/user/login"}
        else:
            dict_msg={"status":"1002","Msg":"未知错误","value":""}
        return jsonify(dict_msg)

# 忘记密码页面
@app.route('/user/forget', methods=['GET', 'POST'])
def fget():
    if request.method=="GET":
        return render_template("forget.html")
    else:
        data=request.json
        email=data.get("email")
        # 判断账号是否存在
        is_exist=base.email_exist(email)
        if not is_exist:            
            dict_msg={"status":"1001","Msg":"邮箱地址错误，请检查","value":""}
        elif type(is_exist) is str:
            dict_msg={"status":"1002","Msg":is_exist,"value":""}
        else:
            validcode=sendMail(email,'【❤H】找回密码：','找回密码')
            if  validcode:
                dict_msg={"status":"1000","Msg":"邮件发送成功,请前往查收","value":"/user/login"}
            else:
                dict_msg={"status":"1001","Msg":"邮件发送失败","value":""}
        return jsonify(dict_msg)
        

# 个人中心
@app.route('/user/home', methods=['GET', 'POST'])
def home():
    if request.method=="GET":
        return render_template("home.html")

if __name__ == '__main__':    
    app.run(host='0.0.0.0',debug=False, port=5001)
    session.permanent = True 
    # 执行完毕必须调用close()方法
    # my01.close()
