import sys
import math

def products():
    x = 999
    while x >= 100:
        y = x
        while y >= 100:
            yield x * y
            y -= 1
        x -= 1

def isPalindrome(n):
    s = str(n)
    return s == s[::-1]

def findMax():
    max = -1
    for i in products():
        if isPalindrome(i) and i > max:
            max = i
    return max

def main(argv):
    print(findMax())

if __name__ == '__main__':
    sys.exit(main(sys.argv))
