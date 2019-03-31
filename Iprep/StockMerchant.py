#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    di = {}
    pairs =0
    for i in range(n):
        if ar[i] in di:
            di[ar[i]].append(ar[i])
        else :
            di[ar[i]]=[ar[i]]
    for k ,v in di.items():
        #print("{} == {}".format(k,len(v)))
        if (len(v) >= 2) :
            pairs += (len(v)//2)
    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))
    
    result = sockMerchant(n, ar)
    #print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
