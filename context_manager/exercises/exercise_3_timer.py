"""
TIMER

Naszym zadaniem jest napisanie klasy context managera realizującą funcjonalności stopera. Funkcja
powinna mierzyć czas wykonania kod pod blokiem with.
* przy wejściu do bloku with uruchamiany jest stoper tzn. zapisywany jest aktualny czas do
  atrybutu self._start. Aby pobrać czas użyj time.time().
* po zakończeniu bloku with chcemy wyświetlić czas z jakim został wykonany ten blok, znowu należy
  użyć time.time() od którego odejmiemy czas startu. Jeśli w bloku wystąpił wyjątek chcemy o tym
  poinformować użytkownika wyświetlając odpowiednią wiadomość. Chcemy go także uciszyć

Zadanie dodatkowe:
Dodajemy implementacje limitu czasu wykonywania bloku. Jeżeli limit zostanie przekroczony, to po
zakończeniu bloku rzucany jest własnoręcznie zdefiniowany wyjątek TooLongExecution. Limit jest
przyjmowany w konstruktorze w parametrze limit z domyślną wartością None. Limit jest zapisywany do
atrybutu.
"""

import time


class Timer:

    def __init__(self, limit=None):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


if __name__ == '__main__':
    with Timer(0.1):
        for n in range(10000000):
            pass
        # raise NotImplementedError('asdss')
