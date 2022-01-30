from datetime import datetime


def disable_at_night(func):
    # dekorator, który wywołuje udekorowaną funkcję tylko w ciągu dnia
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            print('Ala ma kota')
            func()
            print('Kot ma Ale')

    return wrapper


@disable_at_night
def say_something():
    print("Hello world")


@disable_at_night
def func():
    print('Ala ma kota')

# say_something = disable_at_night(func=say_something)


def my_func(func):
    func()


if __name__ == '__main__':
    # variable = say_something
    # variable()
    #
    # my_func(func=say_something)
    say_something()
