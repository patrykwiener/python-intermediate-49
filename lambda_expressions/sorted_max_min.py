def sort_key(x):
    return x[1]


if __name__ == '__main__':
    pairs = [(1, 10), (3, 8), (2, 9)]
    print(sorted(pairs))

    print(sorted(pairs, key=lambda x: x[1]))  # [(3, 8), (2, 9), (1, 10)]

    print(min(pairs))  # (1, 10)
    print(min(pairs, key=lambda x: x[1]))  # (3, 8)
    print(max(pairs, key=lambda x: x[1]))  # (1, 10)
    print(max(pairs, key=lambda x: x[0] * x[1]))  # (3, 8)
