import sys

input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append((int(input()), i))
    
arr.sort()

max_swap = 0
for i in range(n):
    val, idx = arr[i]
    val_dist = idx-i
    if max_swap < val_dist:
        max_swap = val_dist

print(max_swap+1)