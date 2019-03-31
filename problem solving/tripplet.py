#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    arr = []
    aCnt= 0
    bCnt =0

    for i in range(len(a)):
        #print("{}..{}".format(a[i],b[i]))
        if (a[i] > b[i]) :
            aCnt += 1
        if (a[i] < b[i]) :
            bCnt += 1
        #print("acnt={}".format(aCnt))
        #print("bcnt={}".format(bCnt))
    
    arr.append(aCnt)
    arr.append(bCnt)
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
    print(result)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
