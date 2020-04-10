from inspect import getfullargspec
import math


class Overloader:
    functions = {}

    def __init__(self, func):
        Overloader.functions[(func.__name__, len(getfullargspec(func).args))] = func
        self.func = func

    def __call__(self, *args, **kwargs):
        return Overloader.functions[(self.func.__name__, len(args) + len(kwargs))](
            *args, **kwargs
        )


def overload(func):
    return Overloader(func)


@overload
def norm(x, y):
    return math.sqrt(x * x + y * y)


@overload
def norm(x, y, z):
    return abs(x) + abs(y) + abs(z)


print(f"norm(2,4) = {norm(2,4)}")

print(f"norm(2,3,4) = {norm(2,3,4)}")
