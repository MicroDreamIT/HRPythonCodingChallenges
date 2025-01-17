#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    # print(steps, path)
    # 0
    count = 0
    valleys = 0
    in_valley = False
    for i in path:
        if i == 'U':
            count += 1
        else:
            count -=1

    if count < 0 and not in_valley:
        in_valley = True

    if count == 0 and in_valley:
        valleys += 1
        in_valley = False

    return valleys

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
