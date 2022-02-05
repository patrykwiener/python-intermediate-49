"""
PRODUCTS

Napisz trzy funkcje korzystajace z lambda realizujace nastepujace zadania:
* filter - zwraca tylko produkty znajdujace sie w koszyku (in_cart == True)
* reduce - zwraca sume kosztów produktów w liście
* map - zwraca ceny produktów po obniżce o 50%

"""
from dataclasses import dataclass
from functools import reduce
from typing import Callable


@dataclass
class Product:
    id: int
    name: str
    cost: float
    in_cart: bool


PRODUCT_LIST = [
    Product(id=23, name='Monitor', cost=700, in_cart=True),
    Product(id=126, name='Glasses', cost=600, in_cart=False),
    Product(id=16, name='Mouse', cost=100, in_cart=True),
    Product(id=17, name='Keyboard', cost=150, in_cart=True),
    Product(id=65, name='Book', cost=60, in_cart=False),
    Product(id=24, name='Desk lamp', cost=40, in_cart=False),
]

EXPECTED_PRODUCT_LIST = [
    Product(id=23, name='Monitor', cost=700, in_cart=True),
    Product(id=16, name='Mouse', cost=100, in_cart=True),
    Product(id=17, name='Keyboard', cost=150, in_cart=True),
]
EXPECTED_TOTAL_COST = 950
DISCOUNTED_PRICES = [350, 50, 75]

if __name__ == '__main__':
    # obj.in_cart is True
    cart = list(filter(lambda x: x.in_cart, PRODUCT_LIST))
    cart = [product for product in PRODUCT_LIST if product.in_cart]
    assert cart == EXPECTED_PRODUCT_LIST

    total_cost = reduce(lambda total, x: total + x.cost, cart, 0)
    total_cost = sum([product.cost for product in cart])
    assert total_cost == EXPECTED_TOTAL_COST

    discounted_prices = list(map(lambda x: x.cost * 0.5, cart))
    discounted_prices = [product.cost * 0.5 for product in cart]
    assert discounted_prices == DISCOUNTED_PRICES
