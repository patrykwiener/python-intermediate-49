from generators_and_iterators.prime_number_list import is_prime


def prime_generator(n):
    # Generator pozwalający na iterowanie po n liczbach pierwszych
    number = 2
    generated_numbers = 0
    while generated_numbers != n:
        if is_prime(number):
            yield number
            generated_numbers += 1
        number += 1


if __name__ == '__main__':
    gen = prime_generator(1000000)
    a = next(gen)
    b = next(gen)
    c = next(gen)
    d = next(gen)

    for elem in gen:
        print(elem)
