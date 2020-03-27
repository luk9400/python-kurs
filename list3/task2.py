from typing import Iterable


def flatten(items):
    for elem in items:
        if isinstance(elem, Iterable) and not isinstance(elem, (str, bytes)):
            yield from flatten(elem)
        else:
            yield elem


print(list(flatten([[1, 2, ["a", 4, "b", 5, 5, 5]], [4, 5, 6], 7, [[9, [123, [[123]]]], 10]])))
