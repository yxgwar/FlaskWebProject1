# models.py

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_login import UserMixin
import uuid

class User(UserMixin):
    def __init__(self, username):
        self.username = username
        self.id = self.get_id()

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        """save user name, id and password hash to json file"""
        self.password_hash = generate_password_hash(password)
        #写入账号数据

    def verify_password(self, password):
        password_hash = self.get_password_hash()
        if password_hash is None:
            return False
        return check_password_hash(self.password_hash, password)

    def get_password_hash(self):
        #根据用户名获取密码hash值
        return None
        
    def get_id(self):
        if self.username is not None:
            #从数据库中获取id
            return None
        return unicode(uuid.uuid4())

    @staticmethod
    def get(user_id):
        #根据user_id获取user_name
        return User(user_name)