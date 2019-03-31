#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level = 0
    valleys = 0
    for i in s:
        
        if (i == 'U'):
            level += 1 
            print("level + {}".format(level))
        elif (i == 'D'):
            level -= 1
            print("level - {}".format(level))
        
        if (level == 0 and i == 'U'):
            valleys += 1 
    
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)
    #print(result)
    fptr.write(str(result) + '\n')

    fptr.close()