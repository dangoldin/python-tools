#!/usr/bin/env python

import sys
from io import StringIO

import numpy as np
import matplotlib.pyplot as plt

# Usage: pbpaste | ./plotter.py

def read():
    # Assume first row is the header row
    rows = sys.stdin.readlines()

    header = rows[0].strip().split("\t")

    # Assume first column is the x axis (keep as text)
    xs = []
    numerical_data = []
    for line in rows[1:]:
        pieces = line.split("\t")
        xs.append(pieces[0])
        numerical_data.append("\t".join(pieces[1:]))

    c = StringIO(unicode("\n".join(numerical_data)))
    data = np.loadtxt(c)

    return (header, xs, data)

if __name__ == '__main__':
    header, xs, data = read()

    # plt.style.use('ggplot')
    # plt.style.use('bmh')
    plt.style.use('fivethirtyeight')
    plt.figure(1, figsize=(20, 10))

    n_rows, n_cols = data.shape
    first = None
    for series in range(n_cols):
        if series == 0:
            sub = plt.subplot(2, 1, series + 1)
            plt.setp(sub.get_xticklabels(), visible=False)
        else:
            plt.subplot(2, 1, series + 1, sharex=sub)

        plt.plot(data[:,series])
        plt.ylabel(header[series + 1])
        plt.locator_params(axis='x', nbins=10)

        # The last one
        if series == (n_cols - 1):
            plt.xticks(np.arange(len(xs)), xs, rotation=70)

    plt.tight_layout()
    plt.show()
