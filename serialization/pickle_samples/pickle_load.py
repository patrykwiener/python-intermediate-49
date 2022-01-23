import pickle

from serialization.consts import PICKLE_FILE

if __name__ == '__main__':
    with open(PICKLE_FILE, 'rb') as f:
        data = pickle.load(f)
    print(data)
