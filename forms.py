from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

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

class HomeForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    movie = FileField('movie',validators=[FileRequired(), FileAllowed(['mp4'])])
    submit = SubmitField('upload')

class CommentForm(FlaskForm):
    comment = StringField('comment', validators=[DataRequired()])
    submit = SubmitField('comment')

class SearchForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    submit = SubmitField('name')

class MessageForm(FlaskForm):
    message = StringField('message', validators=[DataRequired()])
    submit = SubmitField('message')