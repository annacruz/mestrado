#! /usr/bin/python

import sys
from collections import Counter

arquivo = open(sys.argv[1],'r')
tmp = arquivo.readlines()
numbers = []
for i in tmp:
    numbers.append(int(i.strip()))
print numbers
frequency = Counter(numbers)
print(frequency)

