import sys

input = sys.stdin.readline

n, m = map(int, input().split())

set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

difference_a = len(set_a-set_b)
difference_b = len(set_b-set_a)

print(difference_a+difference_b)