from flask import Blueprint, render_template, request, session, redirect
from flask_login import logout_user
from flask.helpers import url_for
from flask_login.utils import login_required

auth = Blueprint('auth', __name__)


class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password


admin = []
admin.append(Admin(username="Reeves", password="studentskill"))



@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('name', None)
        username = request.form['Uname']
        password = request.form['Pword']

        admin_login = [x for x in admin if x.username == username][0]
        if admin_login and admin_login.password == password:  
            session['name'] = username
            return redirect(url_for('views.homepage'))
    
    return render_template("login.html")


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('/auth.login'))


