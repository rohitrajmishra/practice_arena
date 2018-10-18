#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(a):
    # for i in range(6):
    #     for j in range(6):
    #         print(a[i][j], end=' ')
    #     print()
    ##An hourglass is basically below representation of indices
    # a[i][j]       a[i][j+1]     a[i][j+2]
    #               a[i+1][j+1]
    # a[i+2][j]     a[i+2][j+1]   a[i+2][j+2]

    # loop for i should run (rows-2) times, for j should run [columns-1]

    hourglassSum_list = []

    for i in range(4):
        # hourglassSum_i = 0
        for j in range(4):
            hourglassSum_i_j = 0
            # Print hourglass
            # print("%d   %d  %d" %(a[i][j],a[i][j+1],a[i][j+2]))
            #               a[i+1][j+1]
            # a[i+2][j]     a[i+2][j+1]   a[i+2][j+2]
            hourglassSum_i_j += a[i][j] + a[i][j + 1] + a[i][j + 2]
            hourglassSum_i_j += a[i + 1][j + 1]
            hourglassSum_i_j += a[i + 2][j] + a[i + 2][j + 1] + a[i + 2][j + 2]
            hourglassSum_list.append(hourglassSum_i_j)

    return max(hourglassSum_list)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()