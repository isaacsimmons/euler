import sys
import math

def generateHexagonal(start):
    n = start
    while True:
        yield (2 * n -1) * n
        n += 1

def isTrangular(t):
    n = math.sqrt((2 * t) + 0.25) - 0.5
    return not n % 1

def isPentagonal(p):
    n = math.sqrt(2*p/3.0 + 1.0/36) + (1.0/6)
    return not n % 1

def findTriple(hexStart):
    for hex in generateHexagonal(hexStart):
        if isPentagonal(hex) and isTrangular(hex):
            return hex

def main(argv):
    print("RETURN ", findTriple(144))

if __name__ == '__main__':
    sys.exit(main(sys.argv))
