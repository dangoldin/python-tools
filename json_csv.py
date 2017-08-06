#!/usr/bin/env python

import sys
import json

# python json_csv.py instances.json Reservations.Instances.PublicDnsName,Reservations.Instances.PrivateDnsName

# {'Reservations': {'Instances': {'PrivateDnsName': {}, 'PublicDnsName': {}}}}

def parse_filter_opts(filter_opts):
    """ Convert command line argument to a tree representation """
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

def json_to_csv(json_tree, opts_tree, so_far):
    """ Recursively go down both the option and json tree to extract info we care about """
    keys = opts_tree.keys()
    for key in keys:
        if 'terminal' in opts_tree[key]:
            print json_tree[key],
        else:
            json_tree = json_tree[key]
            if isinstance(json_tree, list):
                for item in json_tree:
                    json_to_csv(item, opts_tree[key], so_far)
            else:
                json_to_csv(json_tree, opts_tree[key], so_far)
    print

if __name__ == '__main__':
    FILENAME = sys.argv[1]
    FILTER_OPTS = sys.argv[2]

    with open(FILENAME, 'r') as f:
        JSON_TREE = json.loads(f.read())

    OPTS_TREE = parse_filter_opts(FILTER_OPTS)

    json_to_csv(JSON_TREE, OPTS_TREE, [])
