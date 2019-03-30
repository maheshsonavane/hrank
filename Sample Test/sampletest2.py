#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the oddNumbers function below.
def oddNumbers(l, r):
    oddsArray = []
    for i in range(l,r+1):
        if (i % 2 != 0):
            oddsArray.append(i)
    return oddsArray

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    r = int(input().strip())
    
    res = oddNumbers(l, r)
    print(res)
    #fptr.write('\n'.join(map(str, res)))
    #fptr.write('\n')

    #fptr.close()
