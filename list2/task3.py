#!/usr/bin/python
""" tolower catalog and subcatalog names """

import os
import sys


def rename(path):
    print(os.listdir())
    for file in os.listdir():
        os.rename(path + '/' + file, path + '/' + file.lower())
        if os.path.isdir(path + '/' + file.lower()):
            rename(path + '/' + file.lower())
    print(os.listdir())


if __name__ == '__main__':
    path = sys.argv[1]
    rename(path)
