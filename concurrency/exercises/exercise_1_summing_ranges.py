"""
SUMMING RANGES

Naszym zadaniem jest napisanie wspolbieznego dodawania kolejnych liczb ciagu liczb od 0 do n
rosnacych o 1. Tzn. an = an-1 + 1, gdzie a1 = 0.
Do napisania mamy kilka funkcji:
* sum_range(start, end) - funkcja realizujaca sumowanie iteracyjne z odpowiedniego zaresu. Zwraca
                        sumę ciągu z przekazanego zakresu
* prepare_threads(threads_number, sequence_number) - na podstawie parametru threads_number dzieli
  zadania tak aby kazdy watek mial po rowno obliczen (dzieli zakres sequence_number na n czesci,
  gdzie n to liczba watkow). Oprocz tego inicjalizuje wątki i laduje je do listy ktora zwroci ta
  funkcja. Wątki są obiektami klasy ThreadWithReturnValue ktora jest juz zdefiniowane w jednym z
  przykladow (nalezy ją zaimportować). W konstruktorze ten klasy musimy przekazac funkcje, ktora
  dany watek bedzie wykonywal oraz w nastepnym parametrze argumenty tej funkcji w postaci listy.
* start_threads(threads) - funckja startuje wszystkie watki
* join_threads(threads) - funkcja oczekuje na zlaczenie watkow, dodatkowo sumuje ich zwrocone
  wartosci i na koncu je zwraca

Główny przebieg programu jest juz zdefiniowany.
"""
import time

from concurrency.threading_with_return_value import ThreadWithReturnValue


def sum_range(start, end):
    pass


def prepare_threads(threads_number, sequence_number):
    pass


def start_threads(threads):
    pass


def join_threads(threads):
    pass


if __name__ == '__main__':
    threads_number = 4
    sequence_number = 1000000

    threads = prepare_threads(threads_number, sequence_number)
    start = time.time()
    start_threads(threads)
    total = join_threads(threads)
    print(time.time() - start)

    assert total == 499999500000

    start = time.time()
    sum_range(0, sequence_number)
    print(time.time() - start)
