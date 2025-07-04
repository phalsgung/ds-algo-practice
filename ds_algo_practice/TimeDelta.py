#!/usr/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    # print(t1)
    # Sun 10 May 2015 13:54:36
    # %a %d %b %Y %H:%M:%S
    # Day dd Mon yyyy hh:mm:ss
    
    time1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    time2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    # print( int((time1 - time2).total_seconds()) )
    return str(abs(int((time1 - time2).total_seconds())))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        # fptr.write(delta + '\n')
        print(delta)

    # fptr.close()
