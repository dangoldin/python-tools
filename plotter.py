#!/usr/bin/env python

import sys
from io import StringIO

import numpy as np
import matplotlib.pyplot as plt

# Usage: pbpaste | ./plotter.py

if __name__ == '__main__':
    # Assume first row is the header row
    rows = sys.stdin.readlines()

    header = rows[0]

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
    plt.plot(data[:,0])
    plt.xticks(np.arange(len(xs)), xs, rotation=70)
    plt.locator_params(axis='x', nbins=10)
    plt.show()
