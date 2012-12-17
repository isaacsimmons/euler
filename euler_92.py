import sys

ones = set()
ones.add(1)

eightyNines = set()
eightyNines.add(89)

def sumSquare(n):
    tmp = n
    sum = 0
    while(tmp > 0):
        digit = tmp % 10
        sum += digit * digit
        tmp /= 10
    return sum

lastCache = sumSquare(9999999)

def isEightyNine(n):
    if (n <= lastCache):
        return not ones.__contains__(n)
    return not ones.__contains__(sumSquare(n))

def cacheIsEightyNine(n):
    if ones.__contains__(n):
        return False
    if eightyNines.__contains__(n):
        return True
    next = sumSquare(n)
    if cacheIsEightyNine(next):
        eightyNines.add(n)
        return True
    else:
        ones.add(n)
        return False


def main(argv):
    print "Caching first ",  lastCache
    for x in xrange(1, lastCache + 1):
        cacheIsEightyNine(x)
    count = 0
    for x in xrange(1, 9999999 + 1):
        if isEightyNine(x):
            count += 1
    print "RESULT = ", count


if __name__ == '__main__':
    sys.exit(main(sys.argv))
