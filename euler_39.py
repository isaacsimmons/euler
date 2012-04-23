import sys
import math

def countIntegralTriangles(p):
    count = 0
    for a in xrange(1, p):
        b = 1.0* (p*p - 2*p*a) / (2*p - 2*a)
        if b >= a and not b % 1:
#            print(a, b, p-a-b, p)
            count += 1
    return count

def main(argv):
    max = 0
    for p in xrange(1001):
        num = countIntegralTriangles(p)
        if num > max:
            print(p)
            max = num

if __name__ == '__main__':
    sys.exit(main(sys.argv))
