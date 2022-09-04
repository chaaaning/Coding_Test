import sys

input = sys.stdin.readline

n = int(input().rstrip())
for i in range(n):
    print("*"*(i+1))