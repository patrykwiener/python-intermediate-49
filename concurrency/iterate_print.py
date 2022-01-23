import threading


def iterate_print(iter):
    # Funkcja wypisująca elementy listy
    for item in iter:
        print(item)


if __name__ == "__main__":
    # tworzenie wątków
    t1 = threading.Thread(target=iterate_print,
                          args=[[i for i in range(20)]])  # wypisywanie kolejnych liczb naturalnych

    t2 = threading.Thread(target=iterate_print,
                          args=["Python"])  # wypisywanie kolejnych znaków napisu

    # uruchomienie wątków
    t1.start()
    t2.start()

    # czekanie z wykonaniem dalszego kodu, aż oba wątki się zakończą
    t1.join()
    t2.join()

    print("Done!")
