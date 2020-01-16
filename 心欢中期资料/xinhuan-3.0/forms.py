
from flask_wtf import FlaskForm
# from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

# from flask_wtf import FlaskForm as aa
# import flask_wtf



class NewPostForm(FlaskForm): 
    ttle=StringField('Title', validators=[DataRequired()])
    yanzheng=SubmitField("FLY-getvercode",validators=[DataRequired()])
    regs=SubmitField("FLY-getvercode2",validators=[DataRequired()])

        # StringField('Title', validators=[DataRequired(), Length(1,50)])
    # title=StringField()   
    # def __init__(self):
    #     self.title =
        
        # StringField('Title', validators=[DataRequired(), Length(1,50)])
        # body = TextAreaField('Body', validators=[DataRequired()])
        # save = SubmitField('Save') # 保存按钮
        # publish = SubmitField('Publish') # 发布按钮