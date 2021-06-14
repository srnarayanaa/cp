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
string   =    lambda: input().strip()
jn      =    lambda x,l: x.join(map(str,l))
strl    =    lambda: list(input().strip())
muli    =    lambda: map(int,input().strip().split())
mulf    =    lambda: map(float,input().strip().split())
muls    =    lambda: map(str, input().strip().split())
seq     =    lambda: list(map(int,input().strip().split()))
