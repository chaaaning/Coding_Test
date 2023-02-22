import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [0] + list(map(int, input().split()))
arrsum, p_sum = [], 0
for i, val in enumerate(arr):
    p_sum+=val
    arrsum.append(p_sum)

result = []    
for _ in range(m):
    start, end = map(int, input().split())
    result.append(arrsum[end] - arrsum[start-1])
    
for r in result:
    print(r)