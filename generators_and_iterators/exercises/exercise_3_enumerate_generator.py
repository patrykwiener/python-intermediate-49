"""
ENUMERATE GENERATOR

Naszym zadaniem jest napisanie generatora bedacego ekwiwalentem wbudowanej funkcji enumerate().
Enumerate zwaraca kolejne krotki z indeksowaniem. Np. dla listy ['Ala', 'ma', 'kota'] po zastosowaniu
na niej enumerate() kazda iteracja po enumerate bedzie zwracac kolejno:
                                    (0, 'Ala')
                                    (1, 'ma')
                                    (2, 'kota')
dokładnie to samo chcemy osiągnąć naszym generatorem.
* generator przyjmuje w parametrze 'iterable' liste, ktora zostanie poddana enumeracji
* pamietajmy ze wartosc poczatkowego indeksu to 0 i kazde nastepne wywolanie zwroci nam indeks o
  jeden wiekszy od poprzedniego
"""


def enumerate_generator(iterable):
    pass


if __name__ == '__main__':
    sample_list = ['Ala', 'ma', 'kota']
    expected_index = 0
    for index, value in enumerate_generator(sample_list):
        assert index == expected_index
        assert value == sample_list[expected_index]
        expected_index += 1
