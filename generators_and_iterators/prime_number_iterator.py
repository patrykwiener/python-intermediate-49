import time

from generators_and_iterators.prime_number_list import is_prime


class PrimeIterator:
    # Iterator pozwalający na iterowanie po n liczbach pierwszych
    def __init__(self, n):
        self.n = n
        self.generated_numbers = 0
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.generated_numbers >= self.n:
            raise StopIteration
        elif is_prime(self.number):
            self.generated_numbers += 1
            return self.number
        return self.__next__()


if __name__ == '__main__':
    start = time.time()
    iter = PrimeIterator(n=3)

    # a = iter.__next__()
    # b = iter.__next__()
    # c = next(iter)
    # d = next(iter)

    for elem in iter:
        print(elem)
    print(time.time() - start)
