#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, render_template,session
from flask import request, make_response,jsonify
from mysql01 import Mysql01
import config
from Islogin import need_login
import time


app = Flask(__name__)
app.config.from_object(config)#加盐

my01 = Mysql01()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        islogin=need_login(app)        
        if not islogin:
            return render_template("Default.html",data={"uid":session.get("uid"),"username":session.get("username")})
        return islogin
    # if request.method == "GET" and islogin:        
    #     return render_template("Default.html",data={"uid":session.get("uid"),"username":session.get("username")})
    else:
        # 判断是否存在        
        username = request.form.get("username")
        pwd = request.form.get("password")        
        result = my01.query("select pwd,uid from user_info where username=%s",[username])
        # print(jsonify({"error":"账号不存在，请确认"}))
        if len(result) == 0:
            return render_template('login.html',data={"username":username,"pwd":pwd},dic={"status":"1","message":"账号不存在，请确认"})
        elif '%s'%result[0][0] == pwd:
            # 写入log
            uid='%s'%result[0][1]
            result=my01.in_up_de("insert into user_loginlogs(loguid)values(%s)",[uid])
            if result=="操作成功":
                session["uid"]=uid
                session["username"]=username
                return render_template("Default.html",data={"uid":uid,"username":username})
            else:
                return render_template('login.html',data={"username":username,"pwd":pwd},dic={"status":"1","message":"登录日志写入失败，请练习系统管理员"})
        else:
            return render_template('login.html',data={"username":username,"pwd":pwd},dic={"status":"2","message":"密码错误，请确认"})

@app.route("/Building", methods=['GET', 'POST'])
def building():
    islogin=need_login(app)
    if islogin:# 判断session 是否有效
        return islogin
    return render_template("Building.html")


@app.route("/chatmain", methods=['GET', 'POST'])
def chating():
    islogin=need_login(app)
    if islogin:# 判断session 是否有效
        return islogin
    return render_template("chatmain.html")


@app.route('/register', methods=['GET'])
def login_from():    
    return render_template("register.html")


@app.route('/register', methods=['POST'])
def register():    
    return "hello world"
    # render_template("register.html")

@app.route('/item_report', methods=['GET'])
def item_report():    
    return render_template("item_report.html")
    # render_template("register.html")

@app.route('/login', methods=['GET'])
def login():    
    return render_template("login.html")

@app.route('/self_center', methods=['GET'])
def self_center():    
    return render_template("self_center.html")


@app.route('/password/<username>', methods=['GET','POST'])
def pwd(username):    
    if request.method=="GET":        
        # username=request.args.get("username")
        return render_template("password.html",data={"username":username})
    else:
        try:
            username=request.form.get("username")
            email=request.form.get("email")
            old_pwd=request.form.get("old_pwd")
            verify=request.form.get("verify")
            new_pwd=request.form.get("new_pwd")
            result=my01.query("select *from user_info where username=%s and email=%s and pwd=%s",[username,email,old_pwd])
            if len(result)>0:
                result=my01.in_up_de("update user_info set pwd=%s,modifyuid=%s,modifydate=%s",[new_pwd,session.get("uid"),time.ctime])
                if result=="操作成功":
                    pass
        except Exception as e:
            pass 

if __name__ == '__main__':    
    app.run(host='0.0.0.0',debug=False, port=5000)
    session.permanent = True 
    # 执行完毕必须调用close()方法
    my01.close()
