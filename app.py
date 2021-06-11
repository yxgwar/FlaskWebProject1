"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
from flask import render_template, request
from flask_ngrok import run_with_ngrok

from forms import LoginForm
from manager import User
from flask_login import login_user, login_required
from flask_login import LoginManager, current_user
from flask_login import logout_user

app = Flask(__name__)
app.config["SECRET_KEY"] = "12345678"
run_with_ngrok(app)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.init_app(app=app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

@app.route('/')
def index():
    return 'hello'

@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_name = request.form.get('username', None)
        password = request.form.get('password', None)
        remember_me = request.form.get('remember_me', False)
        user = User(user_name)
        if user.verify_password(password):
            login_user(user, remember=remember_me)
            return redirect(request.args.get('next') or url_for('main'))
    return render_template('login.html', title = "sign in", form = form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()