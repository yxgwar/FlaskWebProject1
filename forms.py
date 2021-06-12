from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired

#登陆表单
class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember me', default=False)
    sign_in = SubmitField('sign in')

#注册表单
class RegisterForm(FlaskForm):
    username = StringField('username',validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired()])
    submit = SubmitField('sign up')