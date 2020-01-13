
from flask import session,redirect
from datetime import timedelta
def need_login(app):
    app.permanent_session_lifetime = timedelta(minutes=15) # 设置session到期时间    
#     if not session.get('uid'):
#         return redirect("/user/login")
    
