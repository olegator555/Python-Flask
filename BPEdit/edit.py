from flask import Blueprint, request, url_for
from flask import render_template, redirect

from UserDatabase import work_with_db
from BPQuery.main import dbconfig

edit = Blueprint('order', __name__, template_folder='./templates', static_folder='./static')


@edit.route('/', methods=('GET', 'POST'))
def order1():
    hidden_id = request.args.get('id')
    args = request.args.get('args')
    if hidden_id is not None:
        if args == 'remove':
            work_with_db(dbconfig, "delete from lab1.doc_strings where string_id='%s'", hidden_id)
        elif args == 'edit':
            html_args = work_with_db(dbconfig, "select payed_order_no, sum,pay_date from lab1.doc_strings where "
                                               "string_id='%s'", hidden_id)
            return redirect(url_for('.edit_table', no=html_args[0][0], price=html_args[0][1], date=html_args[0][2],
                                    hidden_id=hidden_id))
        return redirect('/order')
    labels = ['Номер оплаченного заказа', 'Цена в месяц, руб.', 'Дата заказа', 'Действие']
    result = work_with_db(dbconfig, "select payed_order_no, sum,pay_date from lab1.doc_strings")
    hidden = work_with_db(dbconfig, "select string_id from lab1.doc_strings")
    return render_template('order.html', labels=labels, content=result, hidden=hidden)


@edit.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        no = request.form.get('no')
        price = request.form.get('price')
        date = request.form.get('date')
        print(no, price, date)
        work_with_db(dbconfig, "insert into lab1.doc_strings(payed_order_no, sum, pay_date) values ('%s','%s', '%s')",
                     (no, price, date))

        return redirect('/order')
    return render_template('add.html')


@edit.route("/edit", methods=('GET', 'POST'))
def edit_table():
    hidden_id = request.args.get('hidden_id')
    if request.method == 'POST':
        no = request.form.get('no')
        price = request.form.get('price')
        date = request.form.get('date')
        work_with_db(dbconfig, "update lab1.doc_strings set payed_order_no='%s', sum='%s', pay_date='%s' where "
                               "string_id='%s'", (no, price, date, hidden_id))
        return redirect('/order')
    no = request.args.get('no')
    price = request.args.get('price')
    date = request.args.get('date')

    return render_template('edit.html', no=no, price=price, date=date)
