from flask import session


def add_to_basket(item_id: str, result: tuple) -> None:
    basket = session.get('basket', [])
    basket.append([item_id, result, 1])
    session['basket'] = basket
    return None


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
