import sys

input = sys.stdin.readline
n = list(map(lambda x: int(x), input().rstrip()))
n.sort(reverse=True)
for s in n:
    print(s, end="")