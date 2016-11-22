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
    dpi = 200

    # Various plots
    plt.figure()
    by_layer = d.groupby('layer')['Cost'].sum().sort_values(ascending=0).plot(kind='bar', sort_columns=True)
    plt.tight_layout()
    plt.savefig('by_layer.png', figsize=(2000/dpi, 2000/dpi), dpi=dpi)

    plt.figure()
    by_product_name = d.groupby('ProductName')['Cost'].sum().sort_values(ascending=0).plot(kind='bar', sort_columns=True)
    plt.tight_layout()
    plt.savefig('by_product_name.png', figsize=(2000/dpi, 2000/dpi), dpi=dpi)

    plt.figure()
    by_usage_type = d.groupby('UsageType')['Cost'].sum().sort_values(ascending=0).plot(kind='bar', sort_columns=True)
    plt.tight_layout()
    plt.savefig('by_usage_type.png', figsize=(2000/dpi, 2000/dpi), dpi=dpi)

if __name__ == '__main__':
    fp = sys.argv[1]

    d = load_file(fp)
    d = add_layer(d)
    plot(d)
