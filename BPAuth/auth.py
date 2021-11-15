from flask import Blueprint, request, session, flash
from flask import render_template, redirect
from UserDatabase import work_with_db
from BPQuery.main import dbconfig

auth = Blueprint('auth', __name__, template_folder='./templates', static_folder='./static')


@auth.route('/', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        _SQL_ = "select user_role from lab2.user_root where login='%s' and password='%s'"
        result = work_with_db(dbconfig, _SQL_, (login, password))
        if result != ():
            session['group_name'] = result[0][0]
            flash(f"Текущий пользователь -  {session.get('group_name','')}", category="success")
            return redirect('/')
        else:
            flash("Ошибка авторизации", category="error")
    return render_template('login.html')

