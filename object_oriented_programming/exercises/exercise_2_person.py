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
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_from_birth_year(cls, name, birth_year) -> 'Person':
        age = date.today().year - birth_year
        return cls(name=name, age=age)


def make_person_from_birth_year(name: str, birth_year: int) -> Person:
    age = date.today().year - birth_year
    return Person(name=name, age=age)


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

    person = make_person_from_birth_year(
        name='Ala',
        birth_year=1840,
    )
    t=0
