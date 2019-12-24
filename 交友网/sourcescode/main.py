#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, render_template
from flask import request, make_response
from mysql01 import Mysql01

app = Flask(__name__)

my01 = Mysql01()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template("login.html")
    else:
        # 判断是否存在
        username = request.form.get("username")
        pwd = request.form.get("password")
        result = my01.query("select pwd from user_info where username=%s", [username])
        if len(result) == 0:
            return "<script>alert('账号不存在，请确认.')</script>"
        elif result == pwd:
            return render_template("Default.html?username=%s"%username)
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
    app.run(debug=True, port=5001)
