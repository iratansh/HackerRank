import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    min_sum, max_sum = 0, 0
    for el in arr[:4]:
        min_sum += el
    for el in arr[1::]:
        max_sum += el
    print(f'{min_sum} {max_sum}')
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
