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
    Product(id=23, name='Desk lamp', cost=40, in_cart=False),
]

EXPECTED_PRODUCT_LIST = [
    Product(id=23, name='Monitor', cost=700, in_cart=True),
    Product(id=16, name='Mouse', cost=100, in_cart=True),
    Product(id=17, name='Keyboard', cost=150, in_cart=True),
]
EXPECTED_TOTAL_COST = 950
DISCOUNTED_PRICES = [350, 50, 75]

if __name__ == '__main__':
    # cart =
    assert cart == EXPECTED_PRODUCT_LIST

    # total_cost
    assert total_cost == EXPECTED_TOTAL_COST

    # discounted_prices =
    assert discounted_prices == DISCOUNTED_PRICES
