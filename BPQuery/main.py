from flask import Blueprint, request
from flask import render_template
from UserDatabase import UserDatabase
from pymysql import connect

main = Blueprint('main', __name__, template_folder='./templates', static_folder='./static')


def work_with_db(dbconfig, _SQL_, name):
    with UserDatabase(dbconfig) as cursor:
        if cursor is None:
            raise ValueError('Курсор не был создан')
        elif cursor:
            cursor.execute(_SQL_ % name)
            schema = [column[0] for column in cursor.description]
            result = []
            for s in cursor.fetchall():
                result.append(dict(zip(schema, s)))
            return result


@main.route('/')
def requests():
    return render_template('choice_list.html')


@main.route('/request1', methods=('GET', 'POST'))
def request1():
    if request.method == 'POST':
        month = request.form.get('month')
        year = request.form.get('year')
        dbconfig = {'host': 'localhost', 'port': 3306, 'user': 'root', 'password': "", 'db': 'Lab1'}
        _SQL_ = "select * from tovar where month(date)='%s' and year(date)='%s';"
        result = work_with_db(dbconfig, _SQL_, (month, year))
        if not result:
            return render_template('request1_data.html', result="")

        return render_template('request1_data.html', result=result)

    return render_template('request1.html')


@main.route('/request2', methods=('GET', 'POST'))
def request2():
    if request.method == 'POST':
        days = request.form.get('days')
        dbconfig = {'host': 'localhost', 'port': 3306, 'user': 'root', 'password': "", 'db': 'Lab1'}
        _SQL_ = "SELECT * FROM Lab1.order where to_days(curdate())-to_days(order_date)<'%s';"
        result = work_with_db(dbconfig, _SQL_, days)
        if not result:
            return render_template('request2_data.html', result="")

        return render_template('request2_data.html', result=result)

    return render_template('request2.html')


@main.route('/request3', methods=('GET', 'POST'))
def request3():
    if request.method == 'POST':
        days = request.form.get('days')
        dbconfig = {'host': 'localhost', 'port': 3306, 'user': 'root', 'password': "", 'db': 'Lab1'}
        _SQL_ = "SELECT status, count(status) FROM lab1.order where(to_days(curdate())-to_days(order_date))<'%s' " \
                "group by status; "
        result = work_with_db(dbconfig, _SQL_, days)
        if not result:
            return render_template('request3_data.html', result="")

        return render_template('request3_data.html', result=result)

    return render_template('request3.html')


@main.route('/request4', methods=('GET', 'POST'))
def request4():
    if request.method == 'POST':
        category = request.form.get('category')
        dbconfig = {'host': 'localhost', 'port': 3306, 'user': 'root', 'password': "", 'db': 'Lab1'}
        _SQL_ = "SELECT category, count(name) FROM lab1.tovar where category = '%s' group by category;"
        result = work_with_db(dbconfig, _SQL_, category)
        if not result:
            return render_template('request4_data.html', result="")

        return render_template('request4_data.html', result=result)

    return render_template('request4.html')


@main.route('/request5', methods=('GET', 'POST'))
def request5():
    if request.method == 'POST':
        status = request.form.get('status')
        dbconfig = {'host': 'localhost', 'port': 3306, 'user': 'root', 'password': "", 'db': 'Lab1'}
        _SQL_ = "select id, sum(summa) from lab1.order where status='%s' group by id;"
        result = work_with_db(dbconfig, _SQL_, status)
        if not result:
            return render_template('request5_data.html', result="")

        return render_template('request5_data.html', result=result)

    return render_template('request5.html')


@main.route('/request6', methods=('GET', 'POST'))
def request6():
    if request.method == 'POST':
        year = request.form.get('year')
        dbconfig = {'host': 'localhost', 'port': 3306, 'user': 'root', 'password': "", 'db': 'Lab1'}
        _SQL_ = "SELECT client_crypt,min(summa) from lab1.order where year(order_date)='%s' and status=2 group by " \
                "client_crypt; "
        result = work_with_db(dbconfig, _SQL_, year)
        if not result:
            return render_template('request6_data.html', result="")

        return render_template('request6_data.html', result=result)

    return render_template('request6.html')