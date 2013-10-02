import sys
import math

def primeFactors(n):
#    List prime factors excluding 1 and the number itself
    orig = n
    i = 2
    root = math.sqrt(n)
    while root >= i:
        while n % i == 0:
            n /= i
            root = math.sqrt(n)
            yield i
        i += 1
    if n != 1:
        yield n

def listDivisors(n):
    primes = list(primeFactors(n))
    values = set()
    for i in range(2**len(primes) - 1):
        divisor = 1
        for idx in range(len(primes)):
            if (1 << idx) & i:
                divisor *= primes[idx]
        if not values.__contains__(divisor):
            values.add(divisor)
            yield divisor

def isAbundant(n):
    return n < sum(listDivisors(n))

def listAbundant(n):
    for i in range(1, n+1):
        if isAbundant(i):
            yield i

def isSumOfTwo(n, list, set):
    for num in list:
        if set.__contains__(n - num):
            return True
        if num > n / 2:
            return False
    return False

def findNonSum(n):
    abundantList = list(listAbundant(n))
    abundantSet = set(abundantList)
    for i in range(1, n+1):
        if not isSumOfTwo(i, abundantList, abundantSet):
            yield i

def main(argv):
    print(sum(findNonSum(28123)))

if __name__ == '__main__':
    sys.exit(main(sys.argv))
