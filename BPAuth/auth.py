from flask import Blueprint, request, session
from flask import render_template

from decor import group_permission_decorator

auth = Blueprint('auth', __name__, template_folder='./templates', static_folder='./static')


@auth.route('/', methods=('GET', 'POST'))
@group_permission_decorator(session)
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        login = request.form.get('login')
        password = request.form.get('password')

    if login == 'admin' and password == 'password':
        session['group_name'] = 'admin'
        return "Logged in"
    return "Not logged"
