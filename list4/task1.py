#!/usr/bin/python
""" time decorator """

from time import time


def time_decorator(func):
    def inner(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print("Total time taken by ", func.__name__, ": ", end - start)
        return result

    return inner


@time_decorator
def func():
    return max([1, 2, 3, 4, 5])

print(func())

