from abc import ABC, abstractmethod


class Osoba(ABC):
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def __str__(self):
        return f"{self.imie} ma {self.wiek} lat"

    @abstractmethod
    def pokaz_finanse(self):
        pass


class Pracownik(Osoba):
    def __init__(self, imie, wiek, stawka, liczba_godzin):
        super().__init__(imie, wiek)
        self.stawka = stawka
        self.liczba_godzin = liczba_godzin

    def pokaz_finanse(self):
        return self.stawka * self.liczba_godzin


class Student(Osoba):
    def __init__(self, imie, wiek, stypendium):
        super().__init__(imie, wiek)
        self.stypendium = stypendium

    def pokaz_finanse(self):
        return self.stypendium


class Unemployed(Osoba):

    def __init__(self, imie, wiek, zasilek, _500: bool):
        super().__init__(imie, wiek)
        self.zasilek = zasilek
        self._500 = _500

    def pokaz_finanse(self):
        return self.zasilek + 500 if self._500 else self.zasilek


class Child(Osoba):

    def pokaz_finanse(self):
        return 0


if __name__ == '__main__':
    os1 = Osoba(imie="Henryk", wiek=54)
    os2 = Pracownik(imie="Jacek", wiek=36, stawka=20, liczba_godzin=160)
    os3 = Student(imie="Agata", wiek=22, stypendium=1000)

    people = [os2, os3]
    for person in people:
        print(person.pokaz_finanse())

    print(os1)
    print(os2)
    print(os3)
