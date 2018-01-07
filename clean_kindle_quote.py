import sys

print "\n".join(line.replace(' "','"').replace(' .','.').replace(' ,',',').replace(' - ','-') for line in sys.stdin)
