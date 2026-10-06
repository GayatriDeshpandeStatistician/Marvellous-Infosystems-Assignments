#Accept file Name & 1 string from user return frequency of that string from file.
import os
import sys
from sys import *

fname = sys.argv[1]

try:
    fhand = open(fname)
    counts = dict()
    for line in fhand:
        words = line.split()
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
    print(counts[sys.argv[2]])

except:
    print('File cannot be opened:', fname)

#Command:python Assignment9_5.py Demo.txt Marvellous