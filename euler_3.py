import sys

def findFactor(n):
    largest = 1
    i = 2
    while n >= i:
        while n % i == 0:
            n /= i
            largest = i
        i += 1
    return largest

def main(argv):
    print("RETURN ", findFactor(600851475143))

if __name__ == '__main__':
    sys.exit(main(sys.argv))
