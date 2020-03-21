#!/usr/bin/python
""" RSA encryption and decryption """

import sys
import random


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def modInverse(a, m):
    m0 = m
    y = 0
    x = 1

    if m == 1:
        return 0

    while a > 1:
        q = a // m

        t = m

        m = a % m
        a = t
        t = y

        y = x - q * y
        x = t

    if x < 0:
        x = x + m0

    return x


def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    g = 0
    while g != 1:
        d = random.randrange(2, phi - 1)
        g = gcd(d, phi)

    e = modInverse(d, phi)

    return (n, e), (n, d)


def miller_rabin(n):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r = 0
    s = n - 1

    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(40):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def create_keys(length):
    low = 2**(length - 1)
    high = 2**length

    p = 0
    while not miller_rabin(p):
        p = random.randrange(low, high)

    q = 0
    while not miller_rabin(q):
        q = random.randrange(low, high)

    pub, prv = generate_keys(p, q)

    with open('key.pub', 'w') as f:
        f.write(hex(pub[0]) + '\n' + hex(pub[1]))

    with open('key.prv', 'w') as f:
        f.write(hex(prv[0]) + '\n' + hex(prv[1]))


def encrypt_char(char, key):
    n, e = key
    return str(pow(ord(char), e, n))


if __name__ == '__main__':
    if sys.argv[1] == '--gen-keys':
        create_keys(int(sys.argv[2]))
    elif sys.argv[1] == '--encrypt':
        pass
    elif sys.argv[1] == '--decrypt':
        pass
