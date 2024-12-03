#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def createRows(n, queen, obstacle):
    number_of_row = []
    for i in obstacle:
        if queen[0] == i[0]:
            if queen[1] > i[1]:
                number_of_row = [[queen[0], j] for j in range(queen[1], n + 1) if j != queen[1]]
            elif queen[1] < i[1]:
                number_of_row = [[queen[0], j] for j in range(1, i[1]) if j != queen[1]]
            else:
                number_of_row = [[queen[0], j] for j in range(1, n + 1) if j != queen[1]]
    return number_of_row


def createColumns(n, queen, obstacle):
    number_of_column = []
    ## q: 4, 3 obs: 2, 3
    pass


def createDialonal(n, queen, obstacle):
    pass


def queensAttack(n, k, r_q, c_q, obstacles):
    number_of_rows = createRows(n, [r_q, c_q], obstacles)
    number_of_columns = createColumns(n, [r_q, c_q], obstacles)
    number_of_diagonals = createDialonal(n, [r_q, c_q], obstacles)

    return len(number_of_rows) + len(number_of_columns) + len(number_of_diagonals)


if __name__ == '__main__':
    # 5
    # 3
    # 4
    # 3[[5, 5], [4, 2], [2, 3]]

    n = 5

    k = 4

    r_q = 4

    c_q = 3

    obstacles = [[5, 5], [4, 2], [2, 3]]

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(result)
