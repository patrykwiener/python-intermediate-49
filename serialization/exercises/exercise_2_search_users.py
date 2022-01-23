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

from serialization.consts import USERS_DATA_FILE


def load_data(filepath):
    with open(filepath) as in_file:
        return json.load(in_file)


def evaluate_attribute(attribute_value, expected_value, operator):
    if operator == 'eq':
        return attribute_value == expected_value
    if operator == 'gt':
        return attribute_value > expected_value
    if operator == 'lt':
        return attribute_value < expected_value
    return False
    # expression = f'{attribute_value} {operator} {expected_value}'
    # return eval(expression)


def search_data(data, attribute, value, operator='eq'):
    filtered_data = []

    for obj in data:
        if evaluate_attribute(
                attribute_value=obj.get(attribute),
                expected_value=value,
                operator=operator,
        ):
            filtered_data.append(obj)
    return filtered_data
    # return [obj for obj in data if obj.get(attribute) == value]


if __name__ == '__main__':
    data = load_data(USERS_DATA_FILE)
    print(
        search_data(
            data=data,
            attribute='age',
            value='30',
            operator='lt'
        )
    )
