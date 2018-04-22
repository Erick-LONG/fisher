from app.forms.auth import RegisterForm
from app.models.user import User
from . import web
from flask import render_template, request


@web.route('/register',methods = ['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)

    return render_template('auth/register.html',form = {'data':{}})


@web.route('/login',methods = ['GET','POST'])
def login():
    pass


@web.route('/reset/password',methods = ['GET','POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>',methods = ['GET','POST'])
def forget_password(token):
    pass