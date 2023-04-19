import sys
import math

input = sys.stdin.readline

m, n = map(int, input().split())

num_list = [i for i in range(n+1)]

for i in range(2, int(math.sqrt(n))+1):
    num = num_list[i]
    if num==0 or num==1:
        num_list[i] = 0
        continue
    for j in range(i+i, n+1, i):
        num_list[j]=0

for i in range(m, n+1):
    if num_list[i] != 0:
        print(num_list[i])