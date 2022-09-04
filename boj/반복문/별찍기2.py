import sys

input = sys.stdin.readline

n = int(input().rstrip())
for i in range(n):
    print(" "*(n-(i+1)), end="")
    print("*"*(i+1))