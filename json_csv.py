#!/usr/bin/env python

import sys
import json

# python json_csv.py instances.json Reservations.Instances.PublicDnsName,Reservations.Instances.PrivateDnsName

# {'Reservations': {'Instances': {'PrivateDnsName': {}, 'PublicDnsName': {}}}}

def parse_filter_opts(filter_ops):
    pieces = filter_opts.split(',')
    tree = {}
    for piece in pieces:
        curr_node = tree
        for idx, selector in enumerate(piece.split('.')):
            if selector not in curr_node:
                curr_node[selector] = {}
            if idx == len(piece.split('.')) - 1:
                curr_node[selector]['terminal'] = True
            curr_node = curr_node[selector]
    return tree

def json_to_csv(json_tree, opts_tree):
    # Recurse along both options and tree
    keys = opts_tree.keys()
    if len(keys) == 1:
        key = keys[0]
        json_tree = json_tree[key]
        print opts_tree
        if 'terminal' in opts_tree[key]:
            print json_tree
            return
        if isinstance(json_tree, list):
            for item in json_tree:
                json_to_csv(item, opts_tree[key])
        else:
            json_to_csv(json_tree, opts_tree[key])

if __name__ == '__main__':
    filename = sys.argv[1]
    filter_opts = sys.argv[2]

    with open(filename, 'r') as f:
        json_tree = json.loads(f.read())

    opts_tree = parse_filter_opts(filter_opts)

    print opts_tree

    json_to_csv(json_tree, opts_tree)
