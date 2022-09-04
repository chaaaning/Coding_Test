import sys

input = sys.stdin.readline

n = int(input().rstrip())
result_list=[]
for _ in range(n):
    a, b = map(int, input().split())
    result_list.append(a+b)
for i,r in enumerate(result_list):
    print(f"Case #{i+1}: {r}")