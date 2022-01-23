"""
PERSON

Naszym zadaniem jest napisanie klasy Person reprezentującej przykładowy opis osoby w systemie.
W tym przykładzie wykorzystamy @classmethod.

Specyfikacja:
* konstruktor przyjmuje dwa patrametry name oraz age, które są zapisywane do atrybutów o
  odpowiednich nazwach
* metoda klasowa (@classmethod) create_from_birth_year - tworzy osobę na podstawie parametrów
  name oraz birth_year. Metoda oblicza wiek osoby na podstawie birth_year. Aby pobrać aktualny rok
  wykorzystaj taką konstrukcję date.today().year
"""

from datetime import date


class Person:
    pass


def make_person_from_birth(name: str, birth_year: int) -> Person:
    pass


if __name__ == '__main__':
    birth_year = 2021
    age = date.today().year - birth_year
    nugat = Person(
        name='Nugat',
        age=age,
    )

    patryk = Person.create_from_birth_year(
        name='Patryk',
        birth_year=1997,
    )

    person = make_person_from_birth(
        name='Ala',
        birth_year=1840,
    )
