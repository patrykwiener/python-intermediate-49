from object_oriented_programming.multiple_inheritance import Osoba


class Student(Osoba):
    CONST = 1

    def __init__(self, imie, wiek, stypendium):
        if self.czy_imie_poprawne(imie):
            # Osoba.__init__(self, imie, wiek)
            # or better super()
            super().__init__(imie, wiek)
            self.stypendium = stypendium

    def pokaz_finanse(self):
        return self.stypendium

    @classmethod
    def stworz_ze_stringa(cls, napis):
        imie, wiek, stypendium = napis.split()
        wiek, stypendium = int(wiek), float(stypendium)
        if cls.czy_imie_poprawne(imie):
            return cls(imie, wiek, stypendium)

    @staticmethod
    def czy_imie_poprawne(imie):
        Student.another_staticmethod()
        return imie[0].isupper() and len(imie) > 3

    @classmethod
    def czy_imie_poprawne(cls, imie):
        cls.another_staticmethod()
        return imie[0].isupper() and len(imie) > 3

    @staticmethod
    def another_staticmethod():
        print('Student')


def czy_imie_poprawne(imie):
    return imie[0].isupper() and len(imie) > 3


class ChildStudent(Student):

    @staticmethod
    def another_staticmethod():
        print('ChildStudent')


if __name__ == '__main__':
    # Student.czy_imie_poprawne(imie='Ala')
    # ChildStudent.czy_imie_poprawne(imie='Ala')

    # student = Student(imie='Patryk', wiek=25, stypendium=500)
    # student.czy_imie_poprawne(imie='Ala')
    #
    stud1 = Student("Małgorzata", 32, 0)
    stud2 = Student.stworz_ze_stringa("Ala 21 600")
    print(stud1)
    print(stud2)
    # print(Student.czy_imie_poprawne("Alicja"))
    # print(stud1.czy_imie_poprawne(stud1.imie))

    # child = ChildStudent.stworz_ze_stringa('Alicja 24 600')
    # t = 0
