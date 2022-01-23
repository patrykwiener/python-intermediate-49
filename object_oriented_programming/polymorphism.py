from object_oriented_programming.multiple_inheritance import Pracownik, Student, PracujacyStudent, Osoba


def sprawdz_finanse(obj: Osoba):
    print(obj.pokaz_finanse())


if __name__ == '__main__':
    os1 = Pracownik('Jaroslaw', 50, 40, 168)
    os2 = Student('Adnrzej', 50, 600)
    os3 = PracujacyStudent('Patryk', 24, 20, 160, 300)

    sprawdz_finanse(os1)  # instancja klasy Pracownik
    sprawdz_finanse(os2)  # instancja klasy Student
    sprawdz_finanse(os3)  # instancja klasy PracujacyStudent
