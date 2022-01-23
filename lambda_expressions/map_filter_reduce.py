from functools import reduce

if __name__ == '__main__':
    items = [1, 2, 3, 4, 5]

    squared = list(map(lambda x: x ** 2, items))  # [1, 4, 9, 16, 25]
    # simple equivalent
    array = []
    for elem in items:
        array.append(elem ** 2)
    # better list comprehension
    # squared = [item ** 2 for item in items]
    squared = [
        item ** 2
        for item
        in items
    ]

    odds = list(filter(lambda x: x % 2 == 1, items))  # [1, 3, 5]
    # list comprehension with filter
    # odds = [item + 2 for item in items if item % 2 == 1]
    odds = [
        item + 2
        for item
        in items
        if item % 2 == 1
    ]

    print(sum(items))

    my_sum = 0
    for item in items:
        # my_sum = my_sum + item
        my_sum += item

    items_sum = reduce(lambda total, item: total + item, items)  # 15
    items_sum = reduce(
        lambda total, item: total + item,
        items,
        120,
    )  # 15

