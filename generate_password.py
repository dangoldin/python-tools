#!/usr/bin/env python

import sys
import random, string

def generate_password(l):
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(l))

if __name__ == '__main__':
    l = 32
    if len(sys.argv) > 1:
        l = int(sys.argv[1])

    print generate_password(l)
