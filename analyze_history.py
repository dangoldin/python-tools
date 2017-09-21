#!/usr/env/bin python

import sys
import re

from collections import Counter

RE_WHITESPACE = re.compile(r'\s+')

def extract_command(line):
    pieces = RE_WHITESPACE.split(line)
    if len(pieces) >= 3:
        return pieces[2]
    return None

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split("\n")

    all_commands = [extract_command(line) for line in lines]
    clean_commands = [c for c in all_commands if c is not None]

    counter = Counter(clean_commands)
    for command, cnt in counter.most_common(100):
        print command, cnt

