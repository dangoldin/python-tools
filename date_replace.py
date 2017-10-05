#! /usr/bin/env python

import datetime
import sys

if __name__ == '__main__':
    string_template, start_str, end_str = sys.argv[1:]

    start = datetime.datetime.strptime(start_str, '%Y-%m-%d')
    end = datetime.datetime.strptime(end_str, '%Y-%m-%d')

    while start < end:
        print string_template.replace('{{ DATE }}', start.strftime('%Y-%m-%d'))
        start = start + datetime.timedelta(days=1)
