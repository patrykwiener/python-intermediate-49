import threading
import timeit

import requests

from context_manager.exercises.exercise_3_timer import Timer

"""
Without threading
----> request ---> result ---> request ---> result ----> request ---> result ---> END

Threading
-----------> request ----> result -\
-----------> request ----> result ---> END
-----------> request ----> result -/
"""

def crawl(url, dest):
    try:
        result = requests.get(url).text
        with open(dest, "a") as f:
            f.write(result)

    except requests.exceptions.RequestException:
        print("Error with URL check!")


def wo_threading_func(urls):
    for url in urls:
        crawl(url, "without_threads.txt")


def with_threading_func(urls):
    threads = []
    for url in urls:
        th = threading.Thread(target=crawl, args=(url, "with_threads.txt"))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()


if __name__ == "__main__":
    urls = [
        "https://jsonplaceholder.typicode.com/comments/1",
        "https://jsonplaceholder.typicode.com/comments/2",
        "https://jsonplaceholder.typicode.com/comments/3"
    ]
    with Timer():
        for _ in range(10):
            wo_threading_func(urls=urls)

    with Timer():
        for _ in range(10):
            with_threading_func(urls)

#     wo_threading = "wo_threading_func(urls)"
#     with_threading = "with_threading_func(urls)"
#
#     setup = '''
# from __main__ import wo_threading_func, with_threading_func
#
# urls = [
#     "https://jsonplaceholder.typicode.com/comments/1",
#     "https://jsonplaceholder.typicode.com/comments/2",
#     "https://jsonplaceholder.typicode.com/comments/3"
# ]
#     '''
#
#     print("Bez watkow:", timeit.timeit(stmt=wo_threading,
#                                        setup=setup,
#                                        number=10))
#     print("Z watkami", timeit.timeit(stmt=with_threading,
#                                      setup=setup,
#                                      number=10))
