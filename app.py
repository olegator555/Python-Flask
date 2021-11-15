import json

from flask import Flask, render_template, session

from BPAuth.auth import auth
from BPQuery.main import main
from BPEdit.edit import edit
from decor import group_validation_decorator

app = Flask(__name__)
app.register_blueprint(main, url_prefix="/requests")
app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(edit, url_prefix="/order")

app.config['SECRET_KEY'] = "abide"
app.config['ACCESS_CONFIG'] = json.load(open('config/access.json'))


@app.route('/')
def base():
    return render_template('base.html')


@app.route('/goodbye')
def goodbye():
    session.clear()
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


if __name__ == '__main__':
    app.run()
