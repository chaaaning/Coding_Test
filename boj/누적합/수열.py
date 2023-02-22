import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
cur_max, pre_sum = -int(1e8), 0

for i in range(0, n-k+1):
    if i==0:
        pre_sum=sum(arr[:i+k])
        cur_max=pre_sum
    else:
        cur_val = pre_sum-arr[i-1]+arr[i+k-1]
        if cur_val > cur_max:
            cur_max = cur_val
        pre_sum = cur_val

print(cur_max)