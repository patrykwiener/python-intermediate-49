if __name__ == '__main__':

    pairs = [(1, 10), (2, 9), (3, 8)]
    sorted(pairs, key=lambda x: x[1])  # [(3, 8), (2, 9), (1, 10)]
    min(pairs)  # (1, 10)
    max(pairs, key=lambda x: x[1])  # (1, 10)
    max(pairs, key=lambda x: x[0] * x[1])  # (3, 8)
