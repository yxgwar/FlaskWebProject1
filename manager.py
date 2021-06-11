from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_login import UserMixin
import json
import uuid
 
# define profile.json constant, the file is used to
# save user name and password
PROFILE_FILE = "profiles.json"
 
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
        with open(PROFILE_FILE, 'w+') as f:
            try:
                profiles = json.load(f)
            except ValueError:
                profiles = {}
            profiles[self.username] = [password, self.id]
            f.write(json.dumps(profiles))
 
    def verify_password(self, password):
        password = self.get_password()
        if password is None:
            return False
        return check_password_hash(self.password, password)
 
    def get_password(self):
        try:
            with open(PROFILE_FILE) as f:
                user_profiles = json.load(f)
                user_info = user_profiles.get(self.username, None)
                if user_info is not None:
                    return user_info[0]
        except IOError:
            return None
        except ValueError:
            return None
        return None
 
    def get_id(self):
        if self.username is not None:
            try:
                with open(PROFILE_FILE) as f:
                    user_profiles = json.load(f)
                    if self.username in user_profiles:
                        return user_profiles[self.username][1]
            except IOError:
                pass
            except ValueError:
                pass
        return unicode(uuid.uuid4())
 
    @staticmethod
    def get(user_id):
        if not user_id:
            return None
        try:
            with open(PROFILE_FILE) as f:
                user_profiles = json.load(f)
                for user_name, profile in user_profiles.iteritems():
                    if profile[1] == user_id:
                        return User(user_name)
        except:
            return None
        return None