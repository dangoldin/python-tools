#! /usr/bin/env python

import sys

if __name__ == '__main__':
    filename, pre, post = sys.argv[1:]

    with open(filename, 'r') as f:
        for line in f:
            print pre + line.strip() + post
