#!/usr/bin/python
""" tolower catalog and subcatalog names """

import os
import sys


def rename(path):
    print(os.listdir())
    for filename in os.listdir():
        os.rename(path + '/' + filename, path + '/' + filename.lower())
        if os.path.isdir(path + '/' + filename.lower()):
            rename(path + '/' + filename.lower())
    print(os.listdir())


if __name__ == '__main__':
    path = sys.argv[1]
    rename(path)
