from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_login import UserMixin
import DB
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
        #self.password_hash = generate_password_hash(password)
        #DB.ac_insert(self.username, self.password_hash)
        DB.ac_insert(self.username, password)

    def verify_password(self, password):
        if password == DB.ac_query(self.username):
            return True
        else:
            return False
        
    def get_id(self):
        id = DB.ac_id(self.username)
        if id is None:
            return uuid.uuid4()
        else:
            return id

    @staticmethod
    def get(user_id):
        user_name = DB.ac_name(user_id)
        return User(user_name)