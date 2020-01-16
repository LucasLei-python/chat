
from modules import *
import datetime
from sqlalchemy import func,text
from sqlalchemy.orm import aliased

def email_exist(email):
    """
        验证邮箱地址是否存在
    """
    try:
        result=User_info.query.filter(User_info.email==email).first()
        if result:            
            return result
    except Exception as e:
        return "Error："+str(e)

def login_check(email,pwd):
    """
        登录验证
    """
    try:
        result=User_info.query.filter(User_info.email==email,User_info.pwd==pwd).first()
        if result is None:
            return "Error:账号密码错误，请确认"
        else:
            return result
    except Exception as e:
        return "Error："+str(e)

def write_logs(uid):
    """
        写入登录日志
    """
    try:
        db.session.add(User_loginlogs(uid,datetime.datetime.now(),None))       
    except Exception as e:
        return "Error："+str(e)

def check_code(email,vercode):
    """
        验证验证码是否过期或正确
    """
    try:       
        query=Vertify_code.query.filter(Vertify_code.email==email,Vertify_code.code==vercode,Vertify_code.inittime>=(datetime.datetime.now()-datetime.timedelta(minutes=250))).order_by(Vertify_code.inittime.desc()).first()
        if not query:
            return "Error:验证码不存在或已过期，请重新获取" 
    except Exception as e:
        return "Error："+str(e)

def insert_user_info(username,pwd,email):
    try:
        db.session.add(User_info(username=username,pwd=pwd,email=email))     
    except Exception as e:
        return "Error："+str(e)
    
def get_info(uid):
    return User_info.query.filter(User_info.uid==uid).first()

def get_kiss(uid):
    return User_sign_in.query.filter(User_sign_in.uid==uid).order_by(User_sign_in.kiss_day.desc()).all()

def insert_kiss(uid,kiss_cout,kiss_day=datetime.datetime.now()):
    try:
        print(datetime.date)
        db.session.add(User_sign_in(uid,kiss_cout,kiss_day))     
    except Exception as e:
        return "Error："+str(e)

def get_circle_detail(id):
    """
        获取详细的动态
    """
    a=aliased(User_life_circle)
    b=aliased(User_info)
    result=db.session.query(a.id.label("cid"),b.uid,b.username,b.user_type,a.class_type,
    a.title,a.content,a.posted_time,a.see_type).join(b,a.uid==b.uid).filter(a.id==id).first()
    return result

# 删除动态
def del_circle(id):
    """删除动态"""
    try:
        aa=User_life_circle.query.filter(User_life_circle.id==id).first()
        result=db.session.delete(aa)
    except Exception as e:
        return "Error："+str(e)

def get_comment_detail(id):
    """
        获取评论详细
    """    
    a=aliased(User_circle_comment)
    b=aliased(User_info)
    return db.session.query(a.uid,a.comment,b.username,b.user_type,a.inittime).join(b,a.uid==b.uid).filter(a.circle_id==id).order_by(a.inittime.desc()).all()
def get_circle(uid=None,sort_type=None,class_type=None):
    """
        多表关联,返回对象列表
    """
    query_list=(1==1)
    sort_text="User_life_circle_1_posted_time desc"
    a=aliased(User_life_circle)
    b=aliased(User_circle_comment)
    c=aliased(User_info)
    d=aliased(User_sign_in)
    if uid:
        query_list=(a.uid==uid)
        if class_type:
            query_list=(a.uid==uid,a.class_type==class_type) 
    if class_type:
        query_list=(a.class_type==class_type) 
    # query_list=tuple(query_list)
    if sort_type=="comment":
        sort_text="comment_count  desc"
    result=db.session.query(c.uid,c.user_type,c.username,a.id,a.class_type,a.see_type,a.title,a.content,a.posted_time,
        db.func.count(b.uid).label("comment_count"),db.func.sum(db.func.ifnull(d.kiss_count,0)).label("kiss_count")
        # db.func.sum(db.func.ifnull(b.kiss,0)).label("kiss_count")
        ).outerjoin(b,
        a.id==b.circle_id).outerjoin(c,
        a.uid==c.uid)\
        .outerjoin(d,d.uid==a.uid).filter(query_list).group_by(c.uid,
        c.user_type,c.username,a.id,a.see_type,a.class_type,a.title,a.content,
        a.posted_time).order_by(text(sort_text)).all()
    # if sort_type=="comment":
    #     result=db.session.query(c.uid,c.user_type,c.username,a.content,a.posted_time,
    #     db.func.count(b.uid).label("comment_count"),
    #     db.func.sum(db.func.ifnull(b.kiss,0)).label("kiss_count")).outerjoin(b,
    #     a.id==b.circle_id).outerjoin(c,
    #     a.uid==c.uid).filter(query_list).group_by(c.uid,
    #     c.user_type,c.username,a.content,
    #     a.posted_time).order_by(text("db.func.count(b.uid).desc()")).all()
    # else:
    #     result=db.session.query(c.uid,c.user_type,c.username,a.content,a.posted_time,
    #     db.func.count(b.uid).label("comment_count"),
    #     db.func.sum(db.func.ifnull(b.kiss,0)).label("kiss_count")).outerjoin(b,
    #     a.id==b.circle_id).outerjoin(c,
    #     a.uid==c.uid).filter(query_list).group_by(c.uid,
    #     c.user_type,c.username,a.content,
    #     a.posted_time).order_by(text(sort_text)).all()
    # print(result)
    return result

def publishing(uid,class_type,see_type,title,content):
    try:        
        db.session.add(User_life_circle(uid,class_type,see_type,title,content))     
    except Exception as e:
        return "Error："+str(e)

def publishing_up(cid,class_type,see_type,title,content):
    try:     
        obj=User_life_circle.query.filter(User_life_circle.id==cid).first()
        obj.class_type=class_type
        obj.see_type=see_type
        obj.title=title
        obj.content=content
        db.session.add(obj)     
    except Exception as e:
        return "Error："+str(e)


# get_circle(sort_type="comment")

def insert_circlement(uid,circle_id,comment):
    try:        
        db.session.add(User_circle_comment(uid,circle_id,comment))     
    except Exception as e:
        return "Error："+str(e)


  

    
