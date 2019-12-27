
from flask import Flask, render_template,session
from datetime import timedelta
def need_login(app):
    app.permanent_session_lifetime = timedelta(minutes=1) # 设置session到期时间    
    if not session.get('uid'):
        return render_template("login.html",data={},dic={"status":"0","message":""})
    
