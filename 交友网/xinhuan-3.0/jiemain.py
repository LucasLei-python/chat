from flask import Blueprint,request,session,jsonify
import base,datetime,os
from modules import *
import json

jie=Blueprint("jie",__name__)

# 写入评论
@jie.route('/jie/reply/',methods=['GET','POST'])
def reply():
    data=request.form
    uid=session.get("uid")
    # comment=data.get("content")
    dict01={}
    if not uid:
        dict01={"status":"1001","Msg":"请先登录"}
    else:
        circle_id=data.get("cid")
        comment=data.get("comment")
        # 写入数据库
        result=base.insert_circlement(uid,circle_id,comment)
        if result:
            dict01={"status":"1002","Msg":"Error:"+result}
        else:
            dict01={"status":"1000","Msg":"提交成功","value":"/"}            
    return dict01

# 上传图片
@jie.route('/api/upload/',methods=['GET','POST'])
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

@jie.route('/jie/reply_detail/',methods=['GET','POST'])
def reply_detail():
    if request.method=="POST":
        cid=request.form.get("cid")
        # 获取明细
        result=base.get_comment_detail(cid)        
        return jsonify(result)
    
# 删除评论
@jie.route('/jie/del',methods=['GET','POST'])
def del_circle():
    cid=request.form.get("cid")
    uid_login=str(session.get("uid"))
    uid_del=request.form.get("uid")
    dict01={}
    if uid_del!=uid_login:
        dict01={"status":"1001","Msg":"您无权限删除,只有作者本人有权限删除跟编辑"}
    else:
        result=base.del_circle(cid)        
        if result:
            dict01={"status":"1002","Msg":result}
        else:
            dict01={"status":"1000","Msg":"删除成功","value":"/"}
    return jsonify(dict01)






  