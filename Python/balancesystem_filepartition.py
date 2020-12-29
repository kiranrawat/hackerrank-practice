#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'mostBalancedPartition' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY parent
#  2. INTEGER_ARRAY files_size
#

def mostBalancedPartition(parent, files_size):
    # Write your code here
    length = len(parent)
    total = [0 for i in range(length)]
    for i in range(0, length):
        temp = i
        while(temp!= -1):
            total[temp] += files_size[i]
            temp = parent[temp]
    min_total = abs(total[0] - 2 * total[1])
    for i in range(2, length):
        if min_total > abs(total[0] - 2 * total[i]):
            min_total = abs(total[0] - 2 * total[i])
    return min_total    
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    parent_count = int(input().strip())

    parent = []

    for _ in range(parent_count):
        parent_item = int(input().strip())
        parent.append(parent_item)

    files_size_count = int(input().strip())

    files_size = []

    for _ in range(files_size_count):
        files_size_item = int(input().strip())
        files_size.append(files_size_item)

    result = mostBalancedPartition(parent, files_size)

    fptr.write(str(result) + '\n')

    fptr.close()