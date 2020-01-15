#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, render_template,session,url_for
from flask import request, make_response,jsonify,redirect,flash,send_from_directory
from mysql01 import Mysql01
from sendemail import *
import config
from Islogin import need_login
import time,datetime
from modules import *
import base,os

#导入sqlalchemy
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
import json

# 导入日志模块
from rizhi import logging

# from forms import NewPostForm

# 将当前的模块构建成flask应用
# 当flask应用构建完成后就可以接受请求并给出响应
# app = Flask(__name__)

app.config.from_object(config)#加盐
app.config.update(
    SECRET_KEY = os.urandom(24),
    # 上传文件夹
    UPLOAD_FOLDER = 'static/upload/',
    # 最大上传大小，当前16MB
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
)

my01 = Mysql01()
my01.in_up_de("update user_info set ")

# 首页
@app.route('/', methods=['GET', 'POST'])
def index():    
    if request.method=="GET":   
        need_login(app)     
        return render_template("index.html")
    else:
        return ""

# 个人设置
@app.route('/user/set', methods=['GET', 'POST'])
def self_set():    
    if request.method=="GET":   
        need_login(app)     
        return render_template("set.html")
    else:
        return ""

# 写入评论
@app.route('/jie/reply/',methods=['GET','POST'])
def reply():
    data=request.form
    uid=session.get("uid")
    # comment=data.get("content")
    circle_id=data.get("circle_id")
    comment=data.get("comment")
    dict01={}
    # 写入数据库
    result=base.User_circle_comment(uid,circle_id,comment)
    if result:
        dict01={"status":"1000","Msg":"提交成功"}
    else:
        dict01={"status":"1002","Msg":"Error:"+result}
    return dict01
    


# 上传图片
@app.route('/api/upload/',methods=['GET','POST'])
def updimg():
    if request.method=="POST":
        f=request.files.get("file")  
        filename=datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.'+f.filename.split('.')[1]
        # 自动创建上传文件夹
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
        # 保存图片
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        url ='/'+app.config['UPLOAD_FOLDER']+filename  
        return jsonify({"status":"0","url":url})        
# 发表个人动态

@app.route('/user/publishing',methods=['GET','POST'])
def publishing():
    if request.method=="GET":
        return  render_template("add.html")
    else:
        data=request.form
        class_type=data.get("class")
        title=data.get("title")
        content=data.get("content")
        dict01={}
        # 写入数据
        result=base.publishing(session.get("uid"),class_type,title,content)
        if result:
            dict01={"status":"1002","Msg":result,"value":""}
        else:
            dict01={"status":"1000","Msg":"发表成功","value":""}
    return redirect("/")

# 获取个人信息
@app.route('/user_info',methods=['GET', 'POST'])
def info():
    if request.method=="POST":
        dic_per={"uid":"","username":"","user_type":""}
        result=base.get_info(session.get("uid"))
        if result:
            dic_per={"uid":result.uid,"username":result.username,"user_type":result.user_type}
        return jsonify(dic_per)
# 登录页面
@app.route('/user/login', methods=['GET', 'POST'])
def login():    
    if request.method=="GET":        
        return render_template("login.html")
    else:
        try:
            data=json.loads(request.get_data(as_text=True), strict=False)
            email=data.get("email")
            pwd=data.get("pass")
            dict_msg={}
            result=base.login_check(email,pwd)       
            if type(result) is str:                 
                dict_msg={"status":"1002","Msg":result,"value":""}
            else:
                session["email"]=email
                session["uid"]=result.uid
                session["username"]=result.username
                if not base.write_logs(result.uid):
                    dict_msg={"status":"1000","Msg":"登录成功","value":"/"}
                else:
                    dict_msg={"status":"1001","Msg":"登录失败","value":""}
                   
        except Exception as e:        
            dict_msg={"status":"1003","Msg":str(e),"value":""}
        logging(email+"登录--->"+dict_msg["Msg"]) 
        return jsonify(dict_msg)
    
# 退出
@app.route('/user/logout')
def logout():
    if request.method=="GET":
        session.clear()
        return redirect("/")# 回到首页

# 建设中页面
@app.route('/building')
def building():
    return render_template('Building.html')

# 首页动态信息
@app.route('/user/circle',methods=['GET','POST'])
def circle():
    if request.method=="POST":
        # 获取信息
        list_info=[] 
        data=request.form.get("sort_type")
        if data=="comment":   
            result=base.get_circle(session.get("uid"),"comment")
        else:
            result=base.get_circle(session.get("uid"))
        for item in result:  
            dict_info={}  
            dict_info["id"]=item.id
            dict_info["uid"]=item.uid       
            dict_info["username"]=item.username
            dict_info["user_type"]=item.user_type   
            dict_info["class_type"]=item.class_type
            dict_info["title"]=item.title
            if not item.title:
                dict_info["title"]=item.content
                if len(item.content)>10:
                    dict_info["title"]=item.content[:10]+'...'            
            dict_info["content"]=item.content
            dict_info["comment_count"]=item.comment_count
            dict_info["kiss_count"]=item.kiss_count
            dict_info["posted_time"]=item.posted_time.strftime("%Y-%m-%d %H:%M:%S")
            
            list_info.append(dict_info)
            del dict_info
    return jsonify(list_info)
        
# 今日签到
@app.route('/user/kiss',methods=['POST','GET'])
def kiss():
    data={}
    if not session.get("uid"):
        data={"status":"1001","msg":"请先登录","experience":"0","days":"0"}
    else:
        result=base.get_kiss(session.get("uid"))#获取当前kiss数                
        add_kiss=5
        days=1   
        if len(result)>1:    
            for i in range(len(result)):  
                print(result[i].kiss_day,result[i+1].kiss_day)              
                if i<len(result)-2 and (result[i].kiss_day-result[i+1].kiss_day).days<=1:
                    days+=1
                else:
                    break 
        # 判断昨天是否有签到,否则为0
        if result:
            data=(datetime.date.today()-result[0].kiss_day).days
            if (datetime.date.today()-result[0].kiss_day).days>1:
                days=0                 
        
        if days>=30:
            add_kiss=20
        elif days>=15:
            add_kiss=20
        elif days>=5:
            add_kiss=10
        else:
            add_kiss=5
           
        # 如果存在需判断是否已经签到了,用于首页加载        
        if request.form.get("type")=="query":
            if datetime.datetime.strftime(result[0].kiss_day,'%Y-%m-%d')==datetime.datetime.now().strftime("%Y-%m-%d"):
                data={"status":"1000","signed":"true","experience":add_kiss,"days":days}
            else:
                data={"status":"1000","signed":"false","experience":add_kiss,"days":days}
        else:
            # 写入表格
            result=base.insert_kiss(session.get("uid"),add_kiss)
            if result:
                data={"status":"1001","msg":result,"experience":"0","days":"0"}
            # 判断可增加
            else:
                data={"status":"1000","signed":"false","experience":add_kiss,"days":days}
    return jsonify(data)
    
# 动态详情
@app.route('/user/detail',methods=['POST','GET'])
def detail():
    if request.method=="GET":
        cid=request.args.get("cid")
        result=base.get_circle_detail(cid)
        title=result.title
        if not title:
            title=result.content
            if len(result.content)>10:
                title=result.content[:10]+'...' 
        return render_template('detail.html',data={"uid":result.uid,
        "username":result.username,"posted_time":result.posted_time,
        "user_type":result.user_type,"class_type":result.class_type,"title":title,
        "content":result.content})
    else:
        return ""

# 注册页面
@app.route('/user/reg', methods=['GET', 'POST'])
def reg():
    if request.method=="GET":        
        return render_template("reg.html")
    else:  
        try:
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
        except Exception as e:
            dict_msg={"status":"1003","Msg":str(e),"value":""}
        logging(email+"注册--->"+dict_msg["Msg"])
        return jsonify(dict_msg)

# 忘记密码页面
@app.route('/user/forget', methods=['GET', 'POST'])
def fget():
    if request.method=="GET":
        return render_template("forget.html")
    else:
        try:
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
        except Exception as e:
            dict_msg={"status":"1001","Msg":"邮件发送失败","value":""}
        logging(email+"注册--->"+dict_msg["Msg"])            
        return jsonify(dict_msg)


# 个人中心
@app.route('/user/home', methods=['GET', 'POST'])
def home():
    if request.method=="GET":
        return render_template("home.html")



if __name__ == '__main__':
    logging("服务启动成功")    
    app.run(host='0.0.0.0',debug=False, port=5000)
    session.permanent = True 
    
    # 执行完毕必须调用close()方法
    # my01.close()
