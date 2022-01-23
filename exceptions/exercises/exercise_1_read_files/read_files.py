"""
READ FILES

Naszym zadaniem jest napisanie dwóch funkcji.
1. read_file(file_path) - odczytyje zawartość wskazanego pliku w postaci listy
2. read_files(file_paths) - odczytuje zawartość wielu plików i zwraca je w postaci listy list

Pliki znajdują się w folderze <project-root>/exceptions/exercises/assets.

-- budowa ścieżek ---
Do budowy ścieżek posłużyć się funkcjami z modułu 'os', który należy zaimportować.
* os.path.dirname(sciezka_do_pliku) - zwraca ścieżkę do folderu w którym znajduje się wskazany plik
* os.path.dirname(__file__) - zwraca ścieżkę do folderu, w którym znajduje się plik, w którym
  jest użyta funkcja
* os.path.join(*paths) - zwraca złączoną ścieżke w danym systemie operacyjnym

--- read_file ---
* jako parametr przyjmuje ścieżke do pliku, którego ma odczytać w trybie odczytu ('r')
* plik należy otworzyć i następnie użyć na pliku metody readlines(), która pobiera wszystkie linie z pliku
* odczytaną wartość należy zwrócić
** waszym obowiązkiem jest przedebugować wywołanie, aby upenić się w jaki formacie są zwracane dane
** należy pamiętać, aby zamknąć plik ZAWSZE!


--- read_files ---
* korzysta z wcześniej napisanej funkcji read_file
* jako parametr przyjmuje listę ścieżek wskazujących na pliki, które należy odczytać
* zwraca listę list zawierającą dane z plików
** obsłużyć przypadek gdy dany plik nie istnieje (FileNotFoundError zostanie rzucony przez read_file).
   Należy wtedy uznać, że zawawrtość nieistniejącego pliku jest równa pustej liście.
"""
import os

print(__file__)
current_file = __file__
exercise_1_read_files = os.path.dirname(current_file)
exercises = os.path.dirname(exercise_1_read_files)

EXERCISES_PATH = os.path.dirname(os.path.dirname(__file__))
ASSETS_PATH = os.path.join(EXERCISES_PATH, 'assets')

PATHS = [
    os.path.join(ASSETS_PATH, 'file1'),
    os.path.join(ASSETS_PATH, 'file2'),
    os.path.join(ASSETS_PATH, 'file22'),
    os.path.join(ASSETS_PATH, 'file3'),
    os.path.join(ASSETS_PATH, 'file4'),
]


def read_file(file_path):
    # file = open(file_path)
    # lines = file.readlines()
    # file.close()
    # return lines
    with open(file_path, encoding='utf-8') as f:
        return f.readlines()


def read_files(file_paths):
    files_content = []

    for file_path in file_paths:
        try:
            lines = read_file(file_path=file_path)
            files_content.append(lines)
        except FileNotFoundError:
            files_content.append([])

    return files_content


if __name__ == '__main__':
    path = os.path.join(EXERCISES_PATH, 'assets', 'file1')
    print(read_file(file_path=path))

    content = read_files(PATHS)
    for file_content in content:
        print(file_content)

    # [
    #     ['Przepis na pizze; cos tam cos tam', 'Przepis na kluski'],
    #     [],  # nieistniejacy plik
    # ]
