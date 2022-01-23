def dummy_func():
    a = 3
    b = [1, 0, 2]
    # b = [elem for elem in b if elem != 0]
    for elem in b:
        try:
            wynik = a / elem
        except ZeroDivisionError as exp:
            print(f'{type(exp)}: {str(exp)}')
            raise ValueError(str(exp))
        except ValueError:
            continue
        # except Exception: - to jest zabronione!!!!!!
        #     print('Hello world')
        print(f"Wynik to: {wynik}")


class MyClass:
    def __init__(self, fullname):
        self.fullname = fullname

    def __str__(self):
        return f'Fullname: {self.fullname}'

    def __int__(self):
        return 10

    # def __add__(self, other):
    #     self.balance += other


if __name__ == '__main__':
    dummy_func()

    obj = MyClass(fullname='Pies Nugat')
    print(str(obj))
    print(int(obj))
    del obj

    # self.wallet += cash
    # self.wallet.add_cash(cash)
