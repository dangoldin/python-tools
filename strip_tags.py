#!/usr/bin/env python

import sys, os
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

if __name__ == '__main__':
    fn = sys.argv[1]

    with open(fn, 'r') as f:
        s = f.read()
        clean = strip_tags(s)
        with open(fn + '.new', 'w') as g:
            g.write(clean)

    os.rename(fn + '.new', fn)
