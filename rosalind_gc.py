def readFASTA(f):
  name = None
  values = []
  for line in f:
    if line[0] is '>':
      if name:
        yield (name, "".join(values))
      name = line[1:].strip()
      values = []
    else:
      values.append(line.strip())
  if name:
    yield (name, "".join(values))
    
def gcContent(sequence):
  count = 0
  for char in sequence:
    if char is 'G' or char is 'C':
      count += 1
  return float(count) / len(sequence)

maxValue = (None, -1.0)
for pair in readFASTA(open('data.txt')):
  density = gcContent(pair[1])
  if density > maxValue[1]:
    maxValue = (pair[0], density)

print maxValue[0]
print str(100 * maxValue[1]) + '%'
