#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    flavour_cost = {}
    for i, value in enumerate(arr):
        if (m - value in flavour_cost):
            flavours = sorted([flavour_cost[m - value] + 1, i + 1])
            return flavours
        flavour_cost[value] = i


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()