#!/usr/bin/python
""" base64 encoder and decoder """

import sys

table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'


def encode(filename):
    result = ''
    with open(filename, 'rb') as f:
        while True:
            batch = f.read(3)
            if not batch:
                break

            if len(batch) != 3:
                batch += int(0).to_bytes(3 - len(batch), 'big')

            bitstring = bin(int(batch.hex(), base=16))[2:].rjust(24, '0')

            for i in range(0, 24, 6):
                print(bitstring[i:i+6])
                result += table[int(bitstring[i:i+6], base=2)]

            print(bitstring)
        return result


def decode(filename):
    result = bytes()
    with open(filename, 'r') as f:
        while True:
            batch = f.read(4)
            if not batch:
                break

            batch_bitstring = ''
            for char in batch:
                batch_bitstring += bin(table.index(char))[2:].rjust(6, '0')

            print(batch_bitstring)
            for i in range(0, 24, 8):
                byte = int(batch_bitstring[i: i + 8],
                           base=2).to_bytes(1, 'big')
                print(byte)
                if byte != b'\x00':
                    result += byte

        return result


if __name__ == '__main__':
    if sys.argv[1] == '--encode':
        print(encode(sys.argv[2]))
    elif sys.argv[1] == '--decode':
        print(decode(sys.argv[2]))
