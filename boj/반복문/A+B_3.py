import sys

input = sys.stdin.readline

n = int(input().rstrip())
result_list=[]
for _ in range(n):
    a, b = map(int, input().split())
    result_list.append(a+b)
for r in result_list:
    print(r)