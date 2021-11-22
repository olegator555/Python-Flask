from flask import Blueprint, request, session
from flask import render_template, redirect

from UserDatabase import work_with_db
from BPQuery.main import dbconfig
from basket.utils import add_to_basket, clear_basket

basket_app = Blueprint('basket', __name__, template_folder='./templates', static_folder='./static')


@basket_app.route('/', methods=('GET', 'POST'))
def list_orders():
    if request.method == 'GET':
        basket = session.get('basket', [])
        items = work_with_db(dbconfig, "select id, name, unit_price, ammount from lab1.tovar")
        return render_template('list_order.html', basket=basket, items=items)
    else:
        item_id = request.form.get('hidden')
        result = work_with_db(dbconfig, "select name,unit_price, ammount from lab1.tovar where id='%s'", item_id)
        if result:
            add_to_basket(item_id, result)
        else:
            return render_template('not_found.html')
        return redirect('/basket')


@basket_app.route('/clear_basket')
def clear_basket_handler():
    clear_basket()
    return redirect("/basket")


@basket_app.route('/buy')
def buy():
    basket = session.get('basket', [])
    for elements in basket:
        work_with_db(dbconfig, "insert into lab1.user_data values('%s', '%s', '%s', '%s')",
                     (elements[0], elements[1][0][0], elements[1][0][1], elements[1][0][2]))
    return redirect("/basket")
