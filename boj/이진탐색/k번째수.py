import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

start, end = 1, k
answer = 0

while start<=end:
    mid = (start+end)//2
    num_of_less = 0
    for i in range(1, n+1):
        num_of_less += min(mid//i, n)
    if num_of_less < k:
        start = mid+1
    else:
        answer = mid
        end = mid-1

print(answer)