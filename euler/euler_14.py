import array
import sys

MAX_CACHE = 100000000
depths = array.array('I', [0] * MAX_CACHE)
depths[0] = 1

def nextTerm(n):
    if n % 2:
        return 3* n + 1
    else:
        return n / 2

def findDepth(n):
    if n < MAX_CACHE and depths[n - 1] != 0:
        return depths[n - 1]
    depth = findDepth(nextTerm(n)) + 1
    if n < MAX_CACHE:
        depths[n - 1] = depth
    return depth

def main(argv):
    max = (1, 1)
    for i in xrange(2, 1000001):
        if i % 100 == 0:
            print "At ", i, max
        depth = findDepth(i)
        if depth > max[1]:
            max = (i, depth)
    print "Result ", max

if __name__ == '__main__':
    sys.exit(main(sys.argv))
