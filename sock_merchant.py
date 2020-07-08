#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    set_ar = set(ar)
    print(set_ar)
    pair = 0
        
    for i in set_ar:
        pair += ar.count(i) // 2
    return pair


if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input())

    ar = list(map(int, input().rstrip().split()))
    print(ar)

    result = sockMerchant(n, ar)
    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()



