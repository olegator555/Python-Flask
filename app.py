from flask import Flask, render_template, request, blueprints
from pymysql.err import ProgrammingError
from pymysql.err import OperationalError
from pymysql import connect
from pymysql.err import OperationalError
from pymysql.err import InterfaceError
from BPQuery.main import main
from UserDatabase import UserDatabase

app = Flask(__name__)
app.register_blueprint(main, url_prefix="/requests")



@app.route('/')
def base():
    return render_template('base.html')


if __name__ == '__main__':
    app.run()
