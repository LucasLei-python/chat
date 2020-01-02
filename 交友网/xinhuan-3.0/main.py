#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, render_template,session
from flask import request, make_response,jsonify
from mysql01 import Mysql01
# import config
# from Islogin import need_login
import time


app = Flask(__name__)
# app.config.from_object(config)#加盐

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
        email=request.form.get("email") 
        pwd=request.form.get("pass") 
        my01.query("select *from user_info where email=%s and pwd=%s",[email,pwd])

# 注册页面
@app.route('/user/reg', methods=['GET', 'POST'])
def reg():
    if request.method=="GET":
        return render_template("reg.html")

# 忘记密码页面
@app.route('/user/forget', methods=['GET', 'POST'])
def fget():
    if request.method=="GET":
        return render_template("forget.html")
# 个人中心
@app.route('/user/home', methods=['GET', 'POST'])
def home():
    if request.method=="GET":
        return render_template("home.html")

if __name__ == '__main__':    
    app.run(host='0.0.0.0',debug=False, port=5001)
    session.permanent = True 
    # 执行完毕必须调用close()方法
    my01.close()
