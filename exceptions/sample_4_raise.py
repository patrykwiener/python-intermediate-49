def dummy_func():
    a = 3
    b = [1, 0, 2]
    for elem in b:
        if elem == 0:
            raise ValueError("Dzielnik nie może być równy zeru")
        wynik = a / elem
        print(f"Wynik to: {wynik}")


if __name__ == '__main__':
   dummy_func()
