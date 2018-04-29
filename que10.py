import collections

with open('test.txt') as f:
    c = collections.Counter(f.read().split())
print (c)