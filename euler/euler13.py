

sum = 0

with open('numbers.txt') as f:
    content = f.readlines()
    for line in content:
        sum += long(line.lstrip())

print sum