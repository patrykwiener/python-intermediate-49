"""
SEARCH USERS

Naszym zadaniem jest napisanie prostego filtra danych uzytkownikow znajdujacych sie w pliku
                            serialization\\assets\\users_data.json
Chcemy napisac funkcje load_data przyjmującą jako parametr ścieżkę do pliku, z którego odczyta
dane json i załaduje do dict, ktory zostanie zwrocony.

W następnym kroku napiszemy funkcje search_data, która będzie filtrowala te dane na podstawie
dostarczonego atrybutu i jego wartości.
* Jako parametry dostaje odczytane dane w postaci listy dictów, nazwę atrybutu, ktory nas interesuje
  i jego wartosc.
* Jako wartość zwracana jest to lista dictów zawierających wskazany atrybut o wskazanej wartości

TIPS:
* odczytane dane dostarczone do funkcji beda juz w formacie listy dictów
* aby sprawdzać każdy element listy (każdy dict) użyjmy pętli for
* musimy zdefiniować listę do któej będziemy dodawać dicty, ktore spełniają warunek naszego filtra
* do sprawdzania wartosci atrybutu danego dicta warto posluzyc sie metoda dict get(<attribute>)

ROZWINIĘCIE ZADANIA
Dodatkowo chcielibysmy rozwinąc mozliwosci funkcji search_data, aby pozwalala nam na filtrowanie
po kilku atrybutach. Czyli np. chcielibysmy moc znalezc wszystkich pracownikow, którzy są
mężczyznami oraz maja 24 lata. Do tego zmodyfikujemy sygnaturę parametrów funkcji search_data i od
teraz będzie ona przyjmowac następujące parametry:
* data - dane odczywane z pliku
* filters - dict zawierający filtry np.:
                {
                    'sex': 'M',
                    'age': 24,
                }
"""

import json
from dataclasses import dataclass

from serialization.consts import USERS_DATA_FILE


# my_dict = {
#     'a': 1,
#     'b': 2,
# }
# my_dict['c']
# my_dict.get('c')

@dataclass
class User:
    id: int
    name: str
    sex: str
    age: int


def load_data(filepath):
    with open(filepath) as f:
        return json.load(f)


def load_to_obj(user_dict):
    return User(
        id=user_dict.get('id'),
        name=user_dict.get('name'),
        age=user_dict.get('age'),
        sex=user_dict.get('sex'),
    )


def search_data(data, attribute, value):
    accepted_dicts = []

    for obj in data:
        if obj.get(attribute) == value:
            user = load_to_obj(user_dict=obj)
            accepted_dicts.append(user)

    return accepted_dicts


# def search_data(data, attribute, value):
#     return [obj for obj in data if obj.get(attribute) == value]


if __name__ == '__main__':
    data = load_data(USERS_DATA_FILE)
    print(
        search_data(
            data=data,
            attribute='age',
            value='32',
        )
    )

    data1 = search_data(
        data=data,
        attribute='age',
        value='32',
    )
    data2 = search_data(
        data=data,
        attribute='age',
        value='33',
    )

    data = [*data1, *data2]
    data1.extend(data2)
