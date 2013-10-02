import sys
import math

fCache = {0 : 1, 1:1}
lastF = 1
sCache = {}

def generateFactorial(n):
    if fCache.has_key(n):
        return fCache[n]
    if fCache.has_key(n - 1):
        f = n * fCache[n-1]
    else:
#        print("FACTORIAL CACHE MISS: ", n)
        f = n * generateFactorial(n - 1)
    if fCache.has_key(n-10):
        del fCache[n-10]
    fCache[n] = f
    return f

ks = list(reversed(xrange(1, 6)))

def sumP(n):
    if sCache.has_key(n):
        sum = sCache[n] % n
    elif sCache.has_key(n - 1):
        sum = sCache[n-1] - generateFactorial(n - 6) + generateFactorial(n - 1)
    else:
#        print("CACHE MISS", n)
        sum = 0
        for k in ks:
            sum += generateFactorial(n - k)

    if sCache.has_key(n - 10):
        del sCache[n - 10]
    sCache[n] = sum
    return sum % n

def sumSumP(start, end):
    sum = 0
    for p in xrange(start, end):
        sum += sumP(p)
    return sum

def isPrime(n):
    for x in xrange(2, int(math.floor(math.sqrt(n))) + 1):
        if not n % x:
            return False
    return True


def main(argv):
#    print("RETURN ", sumP(7))
    print("RETURN ", sumSumP(5, 10**8))
#    print("RETURN ", sumSumP(5, 100))

if __name__ == '__main__':
    sys.exit(main(sys.argv))
