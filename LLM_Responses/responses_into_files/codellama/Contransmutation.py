#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMaximumConsecutiveOnes function below.
def getMaximumConsecutiveOnes(arr):
    max_ones = 0
    current_ones = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            current_ones += 1
        else:
            max_ones = max(max_ones, current_ones)
            current_ones = 0
    return max(max_ones, current_ones)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = getMaximumConsecutiveOnes(arr)

        fptr.write(str(result) + '\n')

    fptr.close()