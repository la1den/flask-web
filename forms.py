from wtforms import Form,StringField
from wtforms.validators import length,email,equal_to

class RegisterForm(Form):
    username = StringField(validators=[length(min=3,max=20,message="请输入正确长度的用户名!")])
    email = StringField(validators=[email(message="请输入正确格式的邮箱!")])
    password = StringField(validators=[length(min=6,max=20,message="请输入正确格式的密码!")])
    confirm_password = StringField(validators=[equal_to("password", message="两次密码不一致!")])
