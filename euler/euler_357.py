import sys
import math

import bisect


import euler_23
import euler_381


def listSmallDivisors(n):
    yield 1
    root = math.floor(math.sqrt(n))

    primeFactors = list()
    divisors = set()

    for factor in smallPrimeFactors(n):
        for i in xrange(2**len(primeFactors) - 1):
            divisor = factor
            for idx in range(len(primeFactors)):
                if (1 << idx) & i:
                    divisor *= primeFactors[idx]
                if divisor > root:
                    continue
            if divisor > root:
                continue
            if not divisors.__contains__(divisor):
                divisors.add(divisor)
                yield divisor
        primeFactors.append(factor)


def contains(list, item):
    i = bisect.bisect_left(list, item)
    if i != len(list) and list[i] == item:
        return True
    return False


def smallPrimeFactors(n):
    #generates all prime factors of a number less than or equal to the
    # square root of that number, excluding 1
    i = 2
    root = math.sqrt(n)
    max = root

    while root >= i:
        while n % i == 0:
            n /= i
            root = math.sqrt(n)
            yield i
        i += 1

    if n != 1 and n <= max:
        yield n


primeCache = [1, 2]
def loadPrimes(max):
    for i in xrange(3, int(math.ceil(max))):
        if isPrime(i):
            primeCache.append(i)

def isPrime(n):
    root = math.floor(math.sqrt(n))
    if primeCache[-1] >= n:
        return contains(primeCache, n)
    for i in xrange(1, len(primeCache)):
        p = primeCache[i]
        if p > root:
            return True
        if not n % p:
            return False
    return True

def isSolution(n):
    for divisor in listSmallDivisors(n):
        if not isPrime(divisor + (n / divisor)):
            return False
    return True

def generateSolutions(max):
    for n in xrange(1, max):
#        if not n % 1000:
#            print n
        if isSolution(n):
            print n
            yield n

def main(argv):
#    n = 2*2*2*5
#    print(n, math.sqrt(n))
#    divisors = sorted(list(euler_23.listDivisors(n)))
#    divisors.append(n)
#    print(divisors)
#    print("========")
#    print(list(smallPrimeFactors(n)))
#    print(list(listSmallDivisors(n)))
#    print(sum(generateSolutions(100000000)))


    loadPrimes(math.sqrt(100000000))
    print("Cached ", len(primeCache), " primes")
    print(sum(generateSolutions(100000000)))
#    print("RETURN ", list(generateSolutions(100000)))

if __name__ == '__main__':
    sys.exit(main(sys.argv))
