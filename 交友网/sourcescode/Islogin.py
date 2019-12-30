
from flask import Flask, render_template,session,redirect,url_for
from datetime import timedelta
def need_login(app):
    app.permanent_session_lifetime = timedelta(minutes=1) # 设置session到期时间    
    if not session.get('uid'):
        # aa=redirect(url_for('login'))
        # return redirect(url_for('login'))
        return render_template("login.html",data={},dic={"status":"0","message":""})
    
