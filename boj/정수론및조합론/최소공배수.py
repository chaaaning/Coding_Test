# import sys
# import math

# input = sys.stdin.readline

# n = int(input().rstrip())
# result_list = []
# for _ in range(n):
#     a, b = map(int, input().split())
#     result_list.append((a*b)//math.gcd(a, b))
# for result in result_list:
#     print(result)

import sys

input = sys.stdin.readline

def gcd(n, k):
    a = max(n,k)
    b = min(n,k)
    while a%b!=0:
        mod_res = a%b
        a, b = b, mod_res
    return min(a, b)

n = int(input())
result = []
for _ in range(n):
    a, b = map(int, input().split())
    result.append((a*b)//gcd(a,b))
    
for r in result:
    print(r)