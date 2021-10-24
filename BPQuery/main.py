import json

from flask import Blueprint, request
from flask import render_template

from UserDatabase import UserDatabase

main = Blueprint('main', __name__, template_folder='./templates', static_folder='./static')
dbconfig = json.load(open('config/db.json'))


def work_with_db(dbconfig, _SQL_, name):
    with UserDatabase(dbconfig) as cursor:
        if cursor is None:
            raise ValueError('Курсор не был создан')
        elif cursor:
            cursor.execute(_SQL_ % name)
            schema = [column[0] for column in cursor.description]
            result = cursor.fetchall();

        return result


@main.route('/')
def requests():
    return render_template('choice_list.html')


@main.route('/request1', methods=('GET', 'POST'))
def request1():
    if request.method == 'POST':
        name = request.form.get('username')
        _SQL_ = "select * from lab2.realty where (cost_per_mounth>'%s')"
        result = work_with_db(dbconfig, _SQL_, name)
        if not result:
            return render_template('request_data.html', result="Такой записи не существует")
        labels = ['Айди', 'площадь', 'цена в месяц']
        return render_template('request_data.html', header='Результат поиска по стоимости', labels=labels,
                               content=result)

    return render_template('request1.html')


@main.route('/request2', methods=('GET', 'POST'))
def request2():
    if request.method == 'POST':
        date1 = request.form.get('username')
        date2 = request.form.get('password')
        _SQL_ = "select * from lab2.order where date between '%s' and '%s'"
        result = work_with_db(dbconfig, _SQL_, (date1, date2))
        if not result:
            return render_template('request_data.html', result="Такой записи не существует")

        labels = ['Айди', 'Имя', 'Дата', 'Количество']
        return render_template('request_data.html', header='Результат поиска по дате', labels=labels,
                               content=result)

    return render_template('request2.html')
