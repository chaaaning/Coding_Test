import sys

input = sys.stdin.readline

n = int(input().rstrip())
result_list=[]

for _ in range(n):
    a, b = map(int, input().split())
    result_list.append((a, b, a+b))

for i,result in enumerate(result_list):
    a, b, r = result
    print(f"Case #{i+1}: {a} + {b } = {r}")