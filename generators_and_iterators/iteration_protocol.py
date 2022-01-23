if __name__ == '__main__':

    a = [1, 2, 3, 4]
    for item in a:
        print(item)

    a = "Ala ma kota"
    for item in a:
        print(item)

    a = {'imie': "Adam", 'nazwisko': "Kowalski"}
    for key, value in a.items():
        print(f'{key}: {value}')
