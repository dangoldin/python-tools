#!/usr/bin/env python

import sys
from io import StringIO

import numpy as np
import matplotlib.pyplot as plt

# Usage: pbpaste | ./plotter.py

if __name__ == '__main__':
    # Assume first row is the header row
    rows = sys.stdin.readlines()

    header = rows[0].strip().split("\t")

    print 'Header', header

    # Assume first column is the x axis (keep as text)
    xs = []
    numerical_data = []
    for line in rows[1:]:
        pieces = line.split("\t")
        xs.append(pieces[0])
        numerical_data.append("\t".join(pieces[1:]))

    c = StringIO(unicode("\n".join(numerical_data)))
    data = np.loadtxt(c)

    # Super minimal plot
    # plt.style.use('ggplot')
    plt.style.use('fivethirtyeight')
    # plt.style.use('bmh')
    plt.figure(1, figsize=(20,10))

    dims = data.shape
    first = None
    for series in range(dims[1]):
        if series == 0:
            sub = plt.subplot(2,1,series+1)
            plt.setp(sub.get_xticklabels(), visible=False)
        else:
            plt.subplot(2,1,series+1,sharex=sub)

        plt.plot(data[:,series])
        plt.ylabel(header[series+1])
        plt.locator_params(axis='x', nbins=10)

        if series == (dims[1] - 1):
            plt.xticks(np.arange(len(xs)), xs, rotation=70)

    plt.tight_layout()
    plt.show()
