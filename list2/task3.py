#!/usr/bin/python
""" tolower catalog and subcatalog names """

import os
import sys


def rename(path):
    for filename in os.listdir(path):
        new_path = path + '/' + filename.lower()
        os.rename(path + '/' + filename, new_path)
        if os.path.isdir(new_path):
            rename(new_path)


if __name__ == '__main__':
    path = sys.argv[1]
    rename(path)
