import sys

input = sys.stdin.readline

n, m = map(int, input().split())

lectures = list(map(int, input().split()))

start, end = 0, 0

for l in lectures:
    if start < l:
        start = l
    end += l
    
while start<=end:
    mid = (start+end)//2
    count, cum_sum = 0, 0
    for i in range(n):
        if cum_sum + lectures[i] > mid:
            count+=1
            cum_sum = 0
        cum_sum += lectures[i]
    if cum_sum != 0:
        count+=1
    if count > m:
        start = mid+1
    else:
        end = mid-1
print(start)