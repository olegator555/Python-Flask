from flask import Blueprint, request
from flask import render_template, redirect
from UserDatabase import work_with_db
from BPQuery.main import dbconfig

edit = Blueprint('order', __name__, template_folder='./templates', static_folder='./static')


@edit.route('/', methods=('GET', 'POST'))
def order1():
    if request.method == 'POST':
        data = request.form.get('hidden')
        _ = work_with_db(dbconfig, "delete from lab2.realty where id_realty='%s'", data)
    labels = ['Метраж', 'Цена в месяц, руб.', 'Действие']
    result = work_with_db(dbconfig, "select square, cost_per_mounth from lab2.realty")
    hidden = work_with_db(dbconfig, "select id_realty from lab2.realty")
    return render_template('order.html', labels=labels, content=result, hidden=hidden)


@edit.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        square = request.form.get('square')
        price = request.form.get('price')
        work_with_db(dbconfig, "insert into lab2.realty(square, cost_per_mounth) values ('%s','%s')", (square, price))
        return redirect('/order')
    return render_template('add.html')
