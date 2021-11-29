from flask import session
from UserDatabase import work_with_db
from BPQuery.main import dbconfig


def add_to_basket(item_id: str, result: tuple) -> None:
    basket = session.get('basket', [])
    basket.append([item_id, result, 1])
    session['basket'] = basket
    return None


def buy() -> None:
    basket = session.get('basket', [])
    for elements in basket:
        work_with_db(dbconfig, "insert into lab2.user_data (id_realty, square, cost_per_month)"
                               " values('%s', '%s', '%s')",
                     (elements[0], elements[1][0][0], elements[1][0][1]))


def clear_basket() -> None:
    """
    Очищает корзину
    :args:
        none

    :return:
        none
    """
    if 'basket' in session:
        session.pop('basket')
