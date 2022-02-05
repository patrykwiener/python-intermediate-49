class FileManager:
    def __init__(self, file_name, mode):
        self.file_obj = None
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.file_obj = open(self.file_name, self.mode)
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()
        return False


if __name__ == '__main__':
    with FileManager('exercises/assets/test-file.txt', 'w') as file:
        raise NotImplementedError('Ala ma kota! Ale fajny kot!')
        file.write('Ala ma kota')
    print('Context manager ends...')
