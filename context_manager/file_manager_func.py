from contextlib import contextmanager


@contextmanager
def file_manager(name, mode):
    f = open(name, mode)
    yield f
    f.close()


file = file_manager('a', 'w')  # open & yield
file_manager('a', 'w')  # close

if __name__ == "__main__":
    with file_manager("test.txt", 'w') as f:
        f.write("Test")
