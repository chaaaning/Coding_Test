import sys
import math

input = sys.stdin.readline
n = int(input().rstrip())
n_fac = str(math.factorial(n))

zero_count = 0
for i in range(len(n_fac)-1, -1, -1):
    if n_fac[i]=="0": zero_count+=1
    else: break
print(zero_count)