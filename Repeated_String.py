#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    len_s = len(s)
    count_a = s.count('a')

    total_number = math.floor(n/len_s * count_a)
    reminder = n//len_s

    remaining = 0
    if reminder > 0:
        remaining = s[0:reminder]

    return total_number+remaining


if __name__ == '__main__':

    s = "ababa"

    n = 3

    result = repeatedString(s, n)

    print(result)