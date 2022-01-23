from copy import deepcopy

from object_oriented_programming.dataclass import Prostokat

if __name__ == '__main__':
    p1 = Prostokat(3, 4)
    p2 = deepcopy(p1)

    lst = [1, p1, 3]

    shallow_copy_lst = list(lst)
    # lub
    # shallow_copy_lst = copy(lst)

    deep_copy_lst = deepcopy(lst)

    lst[1].a = 5  # zmieniamy wartosć boku prostokąta

    print(
        f'list: {lst}\n'
        f'shallow_copy_lst: {shallow_copy_lst}\n'
        f'deep_copy_lst: {deep_copy_lst}'
    )
