import json

from flask import Flask, render_template, request, blueprints, session
from pymysql.err import ProgrammingError
from pymysql.err import OperationalError
from pymysql import connect
from pymysql.err import OperationalError
from pymysql.err import InterfaceError
from BPQuery.main import main
from UserDatabase import UserDatabase
from BPAuth.auth import auth
from decor import group_validation_decorator, group_validation

app = Flask(__name__)
app.register_blueprint(main, url_prefix="/requests")
app.register_blueprint(auth, url_prefix="/auth")

app.config['SECRET_KEY'] = 'abcd'
app.config['ACCESS_CONFIG'] = json.load(open('config/access.json'))


@app.route('/')
def base():
    return render_template('base.html')


@app.route('/goodbye')
def goodbye():
    return render_template('goodbye_page.html')


@app.route('/counter')
@group_validation_decorator
def counter():
    count = session.get('counter', None)
    if count is None:
        session['counter'] = 1
    else:
        session['counter'] = session['counter'] + 1

    return f"Your counter {session['counter']}"


@app.route('/clear_session')
def clear_session():
    session.clear()
    return "Cleared"


if __name__ == '__main__':
    app.run()
