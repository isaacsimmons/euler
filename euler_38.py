import sys
import math

def generatePandigital(n):
    used = [ True, False, False, False, False, False, False, False, False, False ]
    m = 1
    s = ""
    while m <= 8:
        t = m * n
        m += 1
        digits = splitDigits(t)
        for d in digits:
            if used[d]:
                return 0
            used[d] = True
        s += str(t)
        if len(s) == 9:
            return int(s)
        if len(s) > 9:
            return 0


def splitDigits(n):
    digits = []
    while n:
        digits.append(n % 10)
        n /= 10
    return list(reversed(digits))

def generateAll():
    largest = 0
    i = 1
    for i in xrange(1, 10000):
        pan = generatePandigital(i)
        if pan > largest:
            largest = pan
    return largest

def main(argv):
    print(generateAll())

if __name__ == '__main__':
    sys.exit(main(sys.argv))
