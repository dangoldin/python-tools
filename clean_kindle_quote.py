import sys

replacement_map = {
    ' "' : '"',
    ' .' : '.',
    ' ,' : ',',
    ' - ': '-',
    ' : ': ':',
    ' ? ': '?',
}

for line in sys.stdin:
    for k, v in replacement_map.iteritems():
        line = line.replace(k, v)
    print(line)
