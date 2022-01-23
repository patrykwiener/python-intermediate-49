"""
VALIDATE FILES

Naszym zadaniem jest napisanie logiki odpowiedzialnej za sprawdzenie czy dane w podanych plikach
są w poprawnym formacie. Jako poprawny format uznaje się tylko i wyłącznie następujące:

                            <nazwa_przepisu>;<link>

Nasza funkcjonalność powinna zawierać wyświetlnie informacji o liczbie plików posiadających błędy.
Należy użyć funkcji read_files() z poprzedniego zadania.


--- validate_files ---
* jako parametr przyjmuje listę ścieżek do plików (podobnie jak w poprzednim zadaniu)
* odczytuje zawartość podanych plików za pomocą read_files()
* wywołuje operacje walidacji na danych z każdego pliku
* na koniec zwraca informację o liczbie zanalezionych błędów

--- validate_content ---
* funkcja przeprowadzająca walidację na przychodzących danych z jednego pliku
* jako parametr przyjmuje dane z jednego pliku w postaci listy stringów
* jeżeli dana linia nie odpowiada przyjętemu przez na formatowi to rzucany jest utworzony przez nas
  wyjącek FileParsingError
** dodatkowy akceptowalny przypadek linii to taki gdzie jest ona pusta
** należy pamiętać o usuwaniu znaków nowej linii '\n'
** przydatne metody stringa w tym zadaniu: replace(), split()
"""

import os

from exceptions.exercises.exercise_1_read_files.read_files import read_files

EXERCISES_PATH = os.path.dirname(os.path.dirname(__file__))
ASSETS_PATH = os.path.join(EXERCISES_PATH, 'assets')

FILES = [
    os.path.join(ASSETS_PATH, 'file1'),
    os.path.join(ASSETS_PATH, 'file2'),
    os.path.join(ASSETS_PATH, 'file22'),
    os.path.join(ASSETS_PATH, 'file3'),
    os.path.join(ASSETS_PATH, 'file4'),
]


class FileParsingError(Exception):
    pass


def validate_content(file_content):
    for line in file_content:
        # line = line.replace('\n', '')
        line = line.strip()
        if line != '':
            line_list = line.split(';')

            if len(line_list) != 2 or line_list[-1] == '' or line_list[0] == '':
                raise FileParsingError()


def validate_files(files):
    files_content = read_files(files)

    counter = 0
    for file_content in files_content:
        try:
            validate_content(file_content=file_content)
        except FileParsingError:
            counter += 1

    return counter


if __name__ == '__main__':
    # lines = [
    #     'Lody czekoladowe;https://aniagotuje.pl/przepis/domowe-lody-czekoladowe\n',
    #     'Lody czekoladowe;https://aniagotuje.pl/przepis/domowe-lody-czekoladowe\n',
    #     'Beza Pavlova;https://www.kwestiasmaku.com/desery/bezy/pavlova/przepis.html\n',
    # ]
    # validate_content(file_content=lines)
    print(validate_files(FILES))
