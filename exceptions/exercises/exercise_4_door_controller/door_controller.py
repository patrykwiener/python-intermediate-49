"""
DOOR CONTROLLER - cz. 1

Wyobraźmy sobie, że piszemy sterownik do kontroli drzwi. Drzwi mogą się otwierać, zamykać.

Specyfikacja:
*   Tworząc obiekt domyślnie stan drzwi (atrybut prywatny '_is_opened') oraz stan rygla ('_is_locked') są równy False
*   W konstruktorze podajemy takze kod otwierający/odryglowujący nasze drzwi. Jest on zapisywany do atrybutu self._unlock_code
*   Metoda 'is_door_opened' pozwalającą sprawdzić aktualny stan drzwi (czy są otwarte czy zamknięte). Zwraca wartość
    boolowską (True lub False)
*   Metoda 'open' otwiera drzwi poprzez odpowiednie ustawienie atrybutu '_is_opened'.
    Drzwi mogą się otworzyć tylko wtedy gdy nie są zaryglowane. Jezeli drzwi zaryglowane rzucany jest wyjątek DoorLockedError.
*   Metoda 'close' zamyka drzwi analogicznie poprzez odpowiednie ustawienie atrybutu '_is_opened'
*   Metoda 'is_door_locked' pozwala sprawdzic czy drzwi są zaryglowane
*   Metoda 'lock' rygluje nam drzwi
*   Metoda 'unlock' odryglowuje nam drzwi, ale tylko w przypadku gdy podamy odpowiedni kod otwarcia.
    W momencie gdy kod jest niepoprawny rzucany jest wyjątek UnlockCodeError, ktory nalezy samemu stworzyć
"""


class DoorLockedError(Exception):
    pass


class UnlockCodeError(Exception):
    pass


class DoorOpenedError(Exception):
    pass


class DoorController:

    def __init__(self, unlock_code):
        self._is_opened = False
        self._is_locked = False
        self._unlock_code = unlock_code

    def is_door_open(self):
        return self._is_opened

    def is_door_locked(self):
        return self._is_locked

    def open(self):
        if self._is_locked:
            raise DoorLockedError
        self._is_opened = True

    def close(self):
        self._is_opened = False

    def lock(self):
        if self._is_opened:
            raise DoorOpenedError
        self._is_locked = True

    def unlock(self, code):
        # if self._unlock_code == code:
        #     self._is_locked = False
        # else:
        #     raise UnlockCodeError
        self._validate_unlock(code=code)
        self._is_locked = False

    def _validate_unlock(self, code):
        # mozna ale nie trzeba
        if self._unlock_code != code:
            raise UnlockCodeError


if __name__ == '__main__':
    door_controller = DoorController(unlock_code='1234')
    print(door_controller.is_door_open())
    print(door_controller.is_door_locked())
    door_controller.open()
    door_controller.close()
    door_controller.lock()
    door_controller.unlock(code='1234')
    door_controller.lock()
    door_controller.unlock(code='4321')
