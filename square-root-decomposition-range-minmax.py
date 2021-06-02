import sys
import math
import bisect
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from bisect import bisect_left as bl,bisect_right as br

sys.setrecursionlimit(100000000)
MOD=10**9+7

inp     =    lambda: int(input())
string  =    lambda: input().strip()
jn      =    lambda x,l: x.join(map(str,l))
strl    =    lambda: list(input().strip())
muli    =    lambda: map(int,input().strip().split())
mulf    =    lambda: map(float,input().strip().split())
muls    =    lambda: map(str, input().strip().split())
seq     =    lambda: list(map(int,input().strip().split()))

def preprocessMin(ratings, N):
    sparseMin = [][]
    for i in range(0, N):
        sparseMin[i][0] = i 

    j = 1
    while 1 << j <= N:
        i = 0
        while i + (1 << j) - 1 < N:
            if ratings[sparseMin[i][j - 1]] < ratings[sparseMin[i + (1 << (j - 1))][j - 1]]:
                sparseMin[i][j] = sparseMin[i][j - 1]
            else:
                sparseMin[i][j] = sparseMin[i + (1 << (j - 1))][j - 1]
            i += 1
        j += 1
    return sparseMin

def preprocessMax(ratings, N):
    sparseMax = [][]
    for i in range(0, N):
        sparseMax[i][0] = i 

    j = 1
    while 1 << j <= N:
        i = 0
        while i + (1 << j) - 1 < N:
            if ratings[sparseMax[i][j - 1]] > ratings[sparseMax[i + (1 << (j - 1))][j - 1]]:
                sparseMax[i][j] = sparseMax[i][j - 1]
            else:
                sparseMax[i][j] = sparseMax[i + (1 << (j - 1))][j - 1]
            i += 1
        j += 1 
    return sparseMax

def maxQuery(low, high, ratings):
    int l = high - low + 1
    k = log2(l)
    if (ratings[sparseMax[low][k]] >= ratings[sparseMax[low + l - (1<<k)][k]]) 
        return ratings[sparseMax[low][k]]
    else:
        return ratings[sparseMax[high - (1<<k) + 1][k]]

def minQuery(low, high, ratings):
    int l = high - low + 1
    k = log2(l)
    if (ratings[sparseMin[low][k]] <= ratings[sparseMin[low + l - (1<<k)][k]]) 
        return ratings[sparseMin[low][k]]
    else:
        return ratings[sparseMin[high - (1<<k) + 1][k]]

a = seq()
#sparseMin = preprocessMin(a, len(a))
#sparseMax = preprocessMax(a, len(a))
#print(maxQuery(0, 6, a))
