#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, render_template
from flask import request
from .mysql import Mysql

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return "Hello world"
    # render_template("../templates/index.html")


# 需要跳转的页面
@app.route("/Default", methods=['GET', 'POST'])
def maintain():
    return render_template("Default.html")

@app.route('./templates',methods=['GET'])
def login_from():
    return render_template("login.html")

@app.route('./templates',methods=['POST'])
def login():
    return render_template("login.html")


# @app.route('/signin', methods=['GET'])
# def signin_form():
#     return '''<form action="/signin" method="post">
#               <p><input name="username"></p>
#               <p><input name="password" type="password"></p>
#               <p><button type="submit">Sign In</button></p>
#               </form>'''
#
# #从signin页面获取参数值
# @app.route('/signin', methods=['POST'])
# def signin():
#     # 需要从request对象读取表单内容：
#     if request.form['username'] == 'admin' and request.form['password'] == 'password':
#         return '<h3>Hello, admin!</h3>'
#     return '<h3>Bad username or password.</h3>'


if __name__ == '__main__':
    app.run()
