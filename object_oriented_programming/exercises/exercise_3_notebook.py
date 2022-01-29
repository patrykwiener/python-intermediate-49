"""
NOTEBOOK

Naszym zadaniem jest napisanie klasy Notebook reprezentującej laptopa w bazie firmy zajmującej się
sprzedażą komputerów. Do tego chcemy wykorzystać dekorator @dataclass.

Specyfikacja:
* atrybut brand - string zawierający nazwę firmy laptopa
* atrybut model - string zawierający nazwę laptopa np. Yoga 720
* atrybut price - float reprezentujący cenę laptopa
* production_year - int reprezentujący rok produkcji danego laptopa
* screen_size - float określający wielkość przekątnej ekranu w calach
* charger_included - bool określający czy ładowarka jest zawarta w ofercie. Dodatkowo wartość
  domyślna to True oraz atrybut nie powinien być zawarty w reprezentacji repr
* is_second_handed - bool określający czy dany laptop jest używany. Wartość domyślna False
* is_antique - bool określający czy dany laptop jest antykiem. Ten atrybut ma nie byc zawarty w
  konstruktorze. Jego wartość jest obliczana na podstawie atrybutu self.production_year. Jeżeli rok
  produkcji jest mniejszy niz 2000 to antyk (True), w przeciwnym wypadku False. Wartosc powinna byc
  obliczana w metodzie __post_init__.
"""

from dataclasses import dataclass, field


@dataclass
class Notebook:
    brand: str
    model: str
    price: float
    production_year: int
    screen_size: float
    charger_included: bool = field(default=True, repr=False)
    is_second_handed: bool = field(default=False)
    is_antique: bool = field(init=False)

    def __post_init__(self):
        self.is_antique = self.production_year < 2000


if __name__ == '__main__':
    dell = Notebook(
        brand='Dell',
        model='Latitude 7490',
        price=3000,
        production_year=1999,
        screen_size=14.1,
        charger_included=False,
        is_second_handed=True,
    )
    t = 0
