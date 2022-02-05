"""
TIMER

Naszym zadaniem jest napisanie klasy context managera realizującą funcjonalności stopera. Funkcja
powinna mierzyć czas wykonania kodu pod blokiem with.
* przy wejściu do bloku with uruchamiany jest stoper tzn. zapisywany jest aktualny czas do
  atrybutu self._start. Aby pobrać czas użyj time.time().
* po zakończeniu bloku with chcemy wyświetlić czas z jakim został wykonany ten blok, znowu należy
  użyć time.time() od którego odejmiemy czas startu. Jeśli w bloku wystąpił wyjątek chcemy o tym
  poinformować użytkownika wyświetlając odpowiednią wiadomość. Chcemy go także uciszyć

Zadanie dodatkowe:
Dodajmy implementacje limitu czasu wykonywania bloku. Jeżeli limit zostanie przekroczony, to po
zakończeniu bloku rzucany jest własnoręcznie zdefiniowany wyjątek TooLongExecution. Limit jest
przyjmowany w konstruktorze w parametrze limit z domyślną wartością None. Limit jest zapisywany do
atrybutu.
"""

import time


class TooLongExecution(Exception):
    pass


class Timer:

    def __init__(self, limit=None):
        self._start = None
        self._limit = limit

    def __enter__(self):
        self._start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        execution_time = time.time() - self._start
        print(f'Execution took: {execution_time}')

        if exc_type:
            print(f'Exception occurred with type: {exc_type} message: {exc_val}')

        if self._limit and execution_time > self._limit:
            raise TooLongExecution(f'execution: {execution_time} limit: {self._limit}')

        # limit: True; execution_time: True -> True
        # limit: True; execution_time: False -> False
        # limit: False; execution_time: True -> False
        # limit: False; execution_time: False -> False

        return True


if __name__ == '__main__':
    with Timer(limit=0.5):
        for n in range(10000000):
            pass
        raise NotImplementedError('asdss')
