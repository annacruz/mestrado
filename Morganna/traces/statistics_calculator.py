#! /usr/bin/python

import sys
from collections import Counter
from math import sqrt

arquivo = open(sys.argv[1],'r')
tmp = arquivo.readlines()
numbers = []
for element in tmp:
    numbers.append(int(element.strip()))
total_elements = len(numbers)
position = total_elements/2
median = (numbers[position] + numbers[position+1])/2

numbers.sort()
frequency = Counter(numbers).most_common()
mode = frequency[0][0]
frequency.sort()

relative_frequency = []
for x in frequency:
    relative_frequency.append({x[0]:round(float(x[1])/total_elements, 3)})

average = []
for e in relative_frequency:
    key = e.keys()[0]
    value = e.values()[0]
    average.append({key:round(key*value,3)})

total_average = 0
for h in average:
    value = h.values()[0]
    total_average += value

second_moment = []
for i in relative_frequency:
    key = i.keys()[0]
    value = i.values()[0]
    sm = round((key**2)*value,3)
    second_moment.append({key:sm})

total_second_moment = 0
for l in second_moment:
    value = l.values()[0]
    total_second_moment += value

variance = round(total_second_moment - (total_average**2),3)
deviation = round(sqrt(variance),3)
