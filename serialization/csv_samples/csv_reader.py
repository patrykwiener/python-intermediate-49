import csv

from serialization.consts import CSV_FILE

if __name__ == '__main__':

    with open(CSV_FILE, encoding='utf-8') as in_file:
        reader = csv.reader(in_file)

        print(next(reader))
        print(next(reader))
        print(next(reader))
        print(next(reader))
        print(next(reader))

        for row in reader:
            print(row)

# numpy
# pandas
