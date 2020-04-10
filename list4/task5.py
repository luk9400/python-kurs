#!/usr/bin/python

from cmath import exp
from math import pi


class FastBigNum:
    def __init__(self, number):
        self.number = number
        self.length = len(number)

    def __str__(self):
        return self.number

    def omega(self, k, n):
        return exp(-2j * k * pi / n)

    def dft(self, x, n):
        return [
            sum(x[i] * self.omega(i * k, n) if i < len(x) else 0 for i in range(n))
            for k in range(n)
        ]

    def idft(self, x, n):
        return [
            int(
                round(
                    sum(
                        x[i] * self.omega(-i * k, n) if i < len(x) else 0
                        for i in range(n)
                    ).real
                )
                / n
            )
            for k in range(n)
        ]

    def __mul__(self, other):
        x_star = self.dft(
            list(map(int, list("".join([self.number, self.length * "0"])))),
            2 * self.length,
        )
        y_star = self.dft(
            list(map(int, list("".join([other.number, other.length * "0"])))),
            2 * other.length,
        )
        z_star = [x_star[i] * y_star[i] for i in range(2 * self.length)]
        result = self.idft(z_star, 2 * self.length)
        result = result[:-1]
        res = 0
        for i, z in enumerate(result[::-1]):
            res += z * 10 ** i
        return FastBigNum(str(res))


A = "1312312231232131231231231231231231212331233231349"
B = "1212312311223123121312312321321231231112323123231"

a = FastBigNum(A)
b = FastBigNum(B)
print(a * b * a)
