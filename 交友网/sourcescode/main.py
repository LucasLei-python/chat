#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, render_template
from flask import request, make_response,jsonify
from mysql01 import Mysql01

app = Flask(__name__)

my01 = Mysql01()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template("login.html",data={},dic={"status":"0","message":""})
    else:
        # 判断是否存在
        username = request.form.get("username")
        pwd = request.form.get("password")        
        result = my01.query("select pwd from user_info where username=%s",[username])
        # print(jsonify({"error":"账号不存在，请确认"}))
        if len(result) == 0:
            return render_template('login.html',data={"username":username,"pwd":pwd},dic={"status":"1","message":"账号不存在，请确认"})
        elif '%s'%result[0] == pwd:
            # 写入log
            return render_template("Default.html",username=username)
        else:
            return "<script>alert('密码错误，请确认.')</script>"


# 需要跳转的页面
@app.route("/Default", methods=['GET', 'POST'])
def maintain():
    return render_template("Default.html")


@app.route("/Building", methods=['GET', 'POST'])
def building():
    return render_template("Building.html")


@app.route("/chatmain", methods=['GET', 'POST'])
def chating():
    return render_template("chatmain.html")


@app.route('/register', methods=['GET'])
def login_from():
    return render_template("register.html")


@app.route('/register', methods=['POST'])
def login():
    return "hello world"
    # render_template("register.html")


@app.route('/password', methods=['GET','POST'])
def pwd():
    return render_template("password.html")


# 执行完毕必须调用close()方法
my01.close()
if __name__ == '__main__':
    app.run(debug=False, port=5000)
