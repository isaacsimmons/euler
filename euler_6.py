import sys
import math

def squaresums(n):
    s = sum(range(1, n + 1))
    return s * s

def sumsquares(n):
    s = 0
    for i in range(1, n + 1):
        s += i * i
    return s

def diff(n):
    return abs(sumsquares(n) - squaresums(n))

def main(argv):
    print("RETURN ", diff(100))

if __name__ == '__main__':
    sys.exit(main(sys.argv))
