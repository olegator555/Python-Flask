from flask import Blueprint, request, session
from flask import render_template, redirect

from basket.utils import *

basket_app = Blueprint('basket', __name__, template_folder='./templates', static_folder='./static')


@basket_app.route('/', methods=('GET', 'POST'))
def list_orders():
    if request.method == 'GET':
        basket = session.get('basket', [])
        items = work_with_db(dbconfig, "select * from lab2.realty")
        return render_template('list_order.html', basket=basket, items=items)
    else:
        item_id = request.form.get('hidden')
        result = work_with_db(dbconfig, "select square, cost_per_mounth from lab2.realty where id_realty='%s'", item_id)
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
def buy_handler():
    buy()
    clear_basket()
    return redirect("/basket")
