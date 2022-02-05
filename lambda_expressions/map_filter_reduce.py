from functools import reduce

if __name__ == '__main__':
    items = [1, 2, 3, 4, 5]

    # ------- MAP --------
    squared = list(map(lambda x: x ** 2, items))  # [1, 4, 9, 16, 25]

    # simple equivalent
    array = []
    for elem in items:
        array.append(elem ** 2)

    # better list comprehension
    squared = [item ** 2 for item in items]
    # squared = [
    #     item ** 2
    #     for item in items
    # ]

    # ------- FILTER --------

    odds = list(filter(lambda x: x % 2 == 1, items))  # [1, 3, 5]
    squared_odds = list(map(lambda x: x ** 2, odds))
    # list comprehension with filter
    # odds = [item ** 2 for item in items if item % 2 == 1]
    odds = [
        item ** 2
        for item in items
        if item % 2 == 1
    ]

    print(sum(items))

    my_sum = 0
    for item in items:
        # my_sum = my_sum + item
        my_sum += item

    # ------- REDUCE --------
    items = ['a', 'b', 'c']
    items_sum = reduce(lambda total, item: total + item, items)  # 15
    print(items_sum)

    func = lambda total, item: total + item
    total = 0
    for item in items:
        total = func(total, item)

    # [1, 2, 3, 4, 5]
    # 0. total = 0; item = 1; -> total = 1
    # 1. total = 1; item = 2; -> total = 3
    # 2. total = 3; item = 3; -> total = 6
    # 3. total = 6; item = 4; -> total = 10
    # 4. total = 10; item = 5; -> total = 15

    items_sum = reduce(
        lambda total, item: total + item,
        items,
        0,
    )
