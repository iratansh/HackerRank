import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    ratio_pos = 0
    ratio_neg = 0
    ratio_zero = 0
    for el in arr:
        if el > 0:
            ratio_pos += 1
        elif el < 0:
            ratio_neg += 1
        else:
            ratio_zero += 1
    ratio_pos = ratio_pos / len(arr)
    ratio_neg = ratio_neg / len(arr)
    ratio_zero = ratio_zero / len(arr)
    print(f'{"{:,.6f}".format(ratio_pos)}\n{"{:,.6f}".format(ratio_neg)}\n{"{:,.6f}".format(ratio_zero)}')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
