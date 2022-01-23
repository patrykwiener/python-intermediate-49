def func_to_lower(x):
    return x.lower()


if __name__ == '__main__':
    my_lambda = lambda x: x.lower()
    print(my_lambda("HA HA HA"))  # "ha ha ha"
    print(func_to_lower("HA HA HA"))

    square_lambda = lambda x: x ** 2
    print(square_lambda(4))  # 16

    equals_lambda = lambda x, y: x == y
    print(equals_lambda(1, 2))  # False
    print(equals_lambda(1, 1))  # True
