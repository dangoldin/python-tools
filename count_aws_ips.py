#! /usr/bin/env python

import urllib.request
import json

with urllib.request.urlopen('https://ip-ranges.amazonaws.com/ip-ranges.json') as f:
    j = json.loads(f.read().decode('utf-8'))

print('All keys', j.keys())

print('IPV4 prefixes', len(j['prefixes']))

ips = 0
for prefix in j['prefixes']:
    cidr = int(prefix['ip_prefix'].split('/')[1])
    ips += 2**(32-cidr)

print('# IPS', ips)
