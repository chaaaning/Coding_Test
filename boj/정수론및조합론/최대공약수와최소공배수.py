import sys
import math

input = sys.stdin.readline

a, b = map(int, input().split())
answer_gcd = math.gcd(a,b)
print(answer_gcd)
print((a*b)//answer_gcd)