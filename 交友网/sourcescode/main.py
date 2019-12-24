#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, render_template
from flask import request,make_response
from mysql01 import Mysql01


app = Flask(__name__)

my01 = Mysql01()

my01.query("select *from user_info")
my01.close()  # 执行完毕必须调用close()方法


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        return "Hello world"
    # render_template("../templates/index.html")

age=28
# 需要跳转的页面
@app.route("/Default", methods=['GET', 'POST'])
def maintain():

    return render_template("Default.html")


@app.route("/Building", methods=['GET', 'POST'])
def building():
    return render_template("Building.html")

@app.route("/chatmain",methods=['GET','POST'])
def chating():
    return render_template("chatmain.html")


if __name__ == '__main__':
    app.run(debug=True)
