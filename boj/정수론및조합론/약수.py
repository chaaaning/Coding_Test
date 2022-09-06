import sys

input = sys.stdin.readline

num_real_divisor = int(input().rstrip())
real_divisors = list(map(int, input().split()))

if num_real_divisor==1: print(real_divisors[0]**2)
else:
    real_divisors.sort()
    print(real_divisors[0]*real_divisors[-1])