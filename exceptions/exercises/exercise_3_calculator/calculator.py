"""
CALCULATOR

Naszym zadaniem jest napisanie prostego kalkulatora realizującego podstawowe operacje (+, -, /, *).
Kalkulator po uruchomieniu pozwala na wprowadzanie wyrażeń typu <liczba> <operator> <liczba> np.
1 + 3 (liczby oraz operator oddzielone spacją). Po wprowadzeniu wyrażenia i zatwierdzeniu enterem program powinien wyświetlić wynik działania.
Kalkulator działa w nieskończonej pętli. Może być zakończony tylko poprzez wpisanie stringa 'quit'.
Szablon logiki uruchomienia aplikacji w pętli jest już gotowy, należy tylko wypełnić 2 funkcje:

*** parse_input ***
Funkcja odpowiedzialna za walidację oraz parsowanie działania dostarczonego przez użytkownika.
* funkcja zwraca trójelementową tuple zawierającą kolejno (liczba, operator, liczba).
* należy sprawdzić czy wyrażenie składa się z trzech elementów (liczby, operatora, liczby),
  na pewno przyda się tutaj metoda stringa split(). Jeżeli wyrażenie nie składa się z trzech elementów,
  to rzucany jest customowy wyjątek ExpressionError
* należy sprawdzić czy obie liczby podane w działaniu są liczbami, a nie np. literkami. Jeżeli nie
  są liczbami, to rzucany jest customowy wyjątek NotNumberError.

*** calculate ***
Funkcja realizująca działanie na podstawie dostarczonych danych.
* funkcja sprawdza z jakim operator ma doczynienia i realizuje to działanie
* jeżeli podany operator nie jest obsługiwany, czyli nie jest żadnym z +, -, /, *, to rzucany jest
  wyjątek InvalidOperatorError
* funkcja zwraca wynik, który poźniej jest wyświetlany w głównej części programu
"""


def parse_input(user_input):
    pass


def calculate(number1, operator, number2):
    pass


def main_loop():
    while True:
        user_input = input('>>> ')
        if user_input == 'quit':
            return
        number1, operator, number2 = parse_input(user_input)
        result = calculate(number1, operator, number2)
        print(result)


if __name__ == '__main__':
    main_loop()
