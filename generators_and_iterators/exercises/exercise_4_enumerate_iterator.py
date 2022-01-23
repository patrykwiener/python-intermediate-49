"""
ENUMERATE ITERATOR

Zadanie bliźniacze do zadania exercise_3_enumerate_generator z tym, że chcemy rozwiazac ten sam
problem za pomoca iteratora EnumerateIterator.
* w konstruktorze przyjmuje on iterable, czyli liste ktora zostanie poddana enumeracji
* w konstruktorze musimy takze zdefiniowac poczatkowa wartosc indexu - 0
* __iter__ zawsze zwraca 'return self'
* __next__ zawsze zwraca tuple (<index>, <element_listy>)
* __next__ pamietajmy ze musimy wykryc moment przejścia przez całą listę i rzucić wtedy wyjątkiem
  StopIteration(), aby zakonczyc generację.
"""


class EnumerateIterator:

    def __init__(self, iterable):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass


if __name__ == '__main__':
    sample_list = ['Ala', 'ma', 'kota']
    expected_index = 0
    for index, value in EnumerateIterator(sample_list):
        assert index == expected_index
        assert value == sample_list[expected_index]
        expected_index += 1
