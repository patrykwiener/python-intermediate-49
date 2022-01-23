"""
DOOR CONTROLLER - cz. 2

Na podstawie implementacji klasy DoorController chcemy napisać aplikację realizującą kontrole drzwi
i wystawiającą do tego interfejs użytkownika. Logika głownego programu odpowiedzialna za realizacje
przyjęcia danych od użytkownika jest już gotowa (funkcja main_loop())

Specyfikacja klasy DoorInterface:
* w konstruktorze przyjmowany jest obiekt drzwi, które będziemy kontrolować
* funkcja perform_operation przyjmuje jako parametr dane wejściowe od użytkownika.
  Aby dobrze obsłużyć walidacje należy użyć metody stringa split(). W tej metodzie sprawdzana jest
  dostarczana komenda i wykonywana odpowiednia akcja. Np. jezeli użytkowni poda komendę 'open',
  to funkcja realizuje wywołanie odpowiedzialne za otwarcie drzwi.
  Jezeli dana komenda nie istnieje to zwracany jest string 'Unknown operation. Try again...'.
  Jezeli komenda jest pustym stringiem to zwracamy 'Invalid input. Try again...'

Dostępne komendy:
* open - otwiera drzwi. Jezeli operacja się udała zwraca string 'Opened the door.', jeżeli nie
  (zostanie rzucony wyjątek) to zwracamy 'You have to unlock the door before you can open.'.
* close - zamyka drzwi. Zwracany string 'Closed the door.'
* is_open - sprawdza czy drzwi są otwarte. Zwraca True lub False
* is_locked - sprawdza czy drzwi są zaryglowane. Zwraca True lub False
* lock - rygluje drzwi. Zwraca 'Locked the door.'.
* unlock <pin> - odryglowuje drzwi. Jeżeli operacja się powiodłą (poprawny pin) to zwraca
          'The door unlocked successfully!' Jeżeli nie (wystąpi wyjątek) to zwracamy
          'Invalid unlock code. Please try again.'

Logika dla obsługi poszczegolnej komendy ma byc zaimplementowana w chronionej metodzie zgodnie z szablonem
"""

from exceptions.exercises.exercise_4_door_controller.door_controller import (
    DoorController,
    DoorLockedError,
    DoorOpenedError,
    UnlockCodeError,
)


class DoorInterface:

    def __init__(self, door_controller: DoorController):
        self._door_controller = door_controller

    def _open(self):
        try:
            self._door_controller.open()
        except DoorLockedError:
            return 'You have to unlock the door before you can open.'
        return 'Opened the door.'

    def _close(self):
        self._door_controller.close()
        return 'Closed the door.'

    def _is_open(self):
        return self._door_controller.is_door_open()

    def _is_locked(self):
        return self._door_controller.is_door_locked()

    def _lock(self):
        try:
            self._door_controller.lock()
        except DoorOpenedError:
            return 'You have to close the door before you can lock.'
        return 'Locked the door.'

    def _unlock(self, unlock_code):
        try:
            self._door_controller.unlock(code=unlock_code)
        except UnlockCodeError:
            return 'Invalid unlock code. Please try again.'
        return 'The door unlocked successfully!'

    def perform_operation(self, user_input):
        # unlock 1234
        if user_input == '':
            return 'Invalid input. Try again...'

        input_list = user_input.split()
        command = input_list[0]

        if command == 'open':
            return self._open()
        if command == 'close':
            return self._close()
        if command == 'is_opened':
            return self._is_open()
        if command == 'is_locked':
            return self._is_locked()
        if command == 'lock':
            return self._lock()
        if command == 'unlock':
            code = input_list[1]
            return self._unlock(unlock_code=code)
        else:
            return 'Unknown operation. Try again...'


def main_loop():
    door_controller = DoorController('1234')
    door_interface = DoorInterface(door_controller)
    while True:
        user_input = input('>>> ')
        if user_input == 'quit':
            return
        result = door_interface.perform_operation(user_input)
        print(result)


if __name__ == '__main__':
    main_loop()
