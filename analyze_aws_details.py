#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt

def load_file(fp):
    dtype_cols = {
        'UsageQuantity' : 'float64',
        'Rate' : 'float64',
        'Cost' : 'float64',
    }
    return pd.read_csv(fp, dtype=dtype_cols, low_memory=False)

def get_opsworks_layers(d):
    return [l.replace('user:opsworks:layer:','') for l in list(d.columns.values) if 'user:opsworks:layer:' in l]

def add_layer(d):
    opsworks_layers = get_opsworks_layers(d)

    d['layer'] = ''
    for layer in opsworks_layers:
        d.layer[ d['user:opsworks:layer:' + layer].notnull() ] = layer
    return d

def plot(d):
    plt.figure()
    # Plot by layer
    d.groupby('layer')['Cost'].sum().plot(kind='bar')

    plt.show()

if __name__ == '__main__':
    fp = sys.argv[1]

    d = load_file(fp)
    d = add_layer(d)
    plot(d)
