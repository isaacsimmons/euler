

i = 0


def maxDigits():
    for i in xrange(1, 100):
        if 10**(i-1) > 9**5 * i:
            return i


def powerit(n, pow):
    sum = 0
    while n:
        sum += (n % 10) ** pow
        n /= 10
    return sum


def isPowery(n, pow):
    return powerit(n, pow) == n

answer = 0

for i in xrange(2, 10**(maxDigits()-1)):
    if isPowery(i, 5):
        print i
        answer += i


print 'answer', answer

