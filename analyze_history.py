#!/usr/env/bin python

import sys
import re

from collections import Counter

RE_WHITESPACE = re.compile(r'\s+')

def extract_command(line):
    """Get the name of the command executed from a line"""
    pieces = RE_WHITESPACE.split(line)
    if len(pieces) >= 3:
        return pieces[2]
    return None

def analyze_file(fn):
    """Print the most commonly executed commands of a file"""
    with open(fn, 'r') as _:
        lines = _.read().split("\n")

    all_commands = [extract_command(_) for _ in lines]
    clean_commands = [_ for _ in all_commands if _ is not None]

    counter = Counter(clean_commands)
    for command, cnt in counter.most_common():
        print command, cnt

if __name__ == '__main__':
    analyze_file(sys.argv[1])
