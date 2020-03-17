#!/usr/bin/python
""" wordcount """

import sys

def wordcount(filename):
    with open(filename, 'r') as f:
        lines = 0
        words = 0
        max_length = 0
        byte_count = 0
        for line in f.readlines():
            lines += 1
            byte_count += len(bytes(line, 'utf8'))
            words += len(line.split())
            if len(line) > max_length:
                    max_length = len(line)
            
        print('Bytes: ', byte_count) 
        print('Words: ', words)
        print('Lines: ', lines)
        print('Longest line: ', max_length)       
        return byte_count, words, lines, max_length

if __name__ == '__main__':
    filename = sys.argv[1]
    wordcount(filename)