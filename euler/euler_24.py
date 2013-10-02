import sys
import math

def permute(n, len):
    n -= 1 #Zero index fix
    sum = 0
    digits = range(len)
    for power in reversed(range(10)):

        f = math.factorial(power)

        index = n // f
        digit = digits[index]
        digits.remove(digit)
        n %= f
        sum += 10** power *digit
    return sum

def main(argv):
    print("RETURN ", permute(1000000, 10))

if __name__ == '__main__':
    sys.exit(main(sys.argv))
