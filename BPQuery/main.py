import json

from flask import Blueprint, request
from flask import render_template
from UserDatabase import work_with_db
from decor import group_permission_decorator

main = Blueprint('main', __name__, template_folder='./templates', static_folder='./static')
dbconfig = json.load(open('config/db.json'))


@main.route('/')
def requests():
    return render_template('choice_list.html')


@main.route('/request1', methods=('GET', 'POST'))
@group_permission_decorator
def request1():
    if request.method == 'POST':
        month = request.form.get('month')
        year = request.form.get('year')
        _SQL_ = "select * from lab1.tovar where month(date)='%s' and year(date)='%s';"
        result = work_with_db(dbconfig, _SQL_, (month, year))
        if not result:
            return render_template('request_data.html', content="")
        labels = ['Категория', 'Зарезервировано', 'Имя', 'Дата инветаризации', 'Материал', 'Цена за единицу',
                  'Количество', 'Единица измерения', 'Дата', 'id', 'Дата заказа']
        return render_template('request_data.html', header='Результат поиска товара', labels=labels, content=result)

    return render_template('request1.html')


@main.route('/request2', methods=('GET', 'POST'))
@group_permission_decorator
def request2():
    if request.method == 'POST':
        days = request.form.get('days')
        _SQL_ = "SELECT * FROM Lab1.order where to_days(curdate())-to_days(order_date)<'%s';"
        result = work_with_db(dbconfig, _SQL_, days)
        if not result:
            return render_template('request_data.html', content="")
        labels = ['Шифр клиента', 'Статус', 'Номер заказа', 'Сумма', 'Количество позиций в заказе', 'Дата заказа', 'id']
        return render_template('request_data.html', header="Результат поиска заказов за последнее время",
                               labels=labels, content=result)

    return render_template('request2.html')


@main.route('/request3', methods=('GET', 'POST'))
@group_permission_decorator
def request3():
    if request.method == 'POST':
        days = request.form.get('days')
        _SQL_ = "SELECT status, count(status) FROM lab1.order where(to_days(curdate())-to_days(order_date))<'%s' " \
                "group by status; "
        result = work_with_db(dbconfig, _SQL_, days)
        if not result:
            return render_template('request_data.html', content="")
        labels = ['Статус', 'Количество']
        return render_template('request_data.html', header="Результат подсчета заказов по статусам", labels=labels,
                               content=result)

    return render_template('request3.html')


@main.route('/request4', methods=('GET', 'POST'))
@group_permission_decorator
def request4():
    if request.method == 'POST':
        category = request.form.get('category')
        _SQL_ = "SELECT category, count(name) FROM lab1.tovar where category = '%s' group by category;"
        result = work_with_db(dbconfig, _SQL_, category)
        if not result:
            return render_template('request_data.html', content="")
        labels = ['Категория', 'Количество']
        return render_template('request_data.html', header='Результат подсчета товаров в категории', labels=labels,
                               content=result)

    return render_template('request4.html')


@main.route('/request5', methods=('GET', 'POST'))
@group_permission_decorator
def request5():
    if request.method == 'POST':
        status = request.form.get('status')
        _SQL_ = "select id, sum(summa) from lab1.order where status='%s' group by id;"
        result = work_with_db(dbconfig, _SQL_, status)
        if not result:
            return render_template('request_data.html', content="")
        labels=['id', 'Сумма']
        return render_template('request_data.html', header='Общая стоимость заказов', labels=labels, content=result)

    return render_template('request5.html')


@main.route('/request6', methods=('GET', 'POST'))
@group_permission_decorator
def request6():
    if request.method == 'POST':
        year = request.form.get('year')
        _SQL_ = "SELECT client_crypt,min(summa) from lab1.order where year(order_date)='%s' and status=2 group by " \
                "client_crypt; "
        result = work_with_db(dbconfig, _SQL_, year)
        if not result:
            return render_template('request_data.html', result="")
        labels=['Шифр клиента', 'Минимальная сумма']
        return render_template('request_data.html', header='Минимальная стоимость оплаченного заказа', labels=labels,
                               content=result)

    return render_template('request6.html')
