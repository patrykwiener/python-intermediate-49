import pickle

from serialization.consts import PICKLE_FILE

data = {
    'a': [1, 2.0, 3, 4 + 6j],
    'b': ("Ala ma kota", "Programowanie w pythonie jest super"),
    'c': [False, True, False]
}

if __name__ == '__main__':
    with open(PICKLE_FILE, 'wb') as f:
        pickle.dump(data, f)
