import sys
import math

sys.setrecursionlimit(100000)

input = sys.stdin.readline

n = int(input())

def isPrNum(x):
    if x==1: return False
    if x==2: return True
    for i in range(2, int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

def dfs(num):
    if len(str(num))==n:
        print(num)
    else:
        for i in range(1, 10):
            if i%2==0: continue
            if isPrNum(num*10+i):
                dfs(num*10+i)
                
dfs(2)
dfs(3)
dfs(5)
dfs(7)