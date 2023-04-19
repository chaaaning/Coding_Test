import sys
import math

input = sys.stdin.readline

n = int(input())

result = n  # n은 소인수를 제외하고 남은 수, result는 소인수를 제외한 갯수
for p in range(2, int(math.sqrt(n))+1):
    if n%p==0:
        result -= result//p
        while n%p == 0:
            n = n//p

if n > 1:
    result -= result//n

print(result)