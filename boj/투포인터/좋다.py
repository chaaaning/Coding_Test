import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

def is_good(arr, target, e):
    if len(arr)<2:
        return False
    else:
        start, end = 0, e
        while start < end:
            p_sum = arr[start]+arr[end]
            if p_sum < target: start+=1
            elif p_sum > target: end-=1
            else:
                return True
    return False

ans = 0

for i in range(n):
    if i==0: sub_arr = arr[i+1:]
    elif i==n-1: sub_arr = arr[:i]
    else: sub_arr = arr[:i]+arr[i+1:]
    if is_good(sub_arr, arr[i], n-2): ans+=1
    
print(ans)


'''
10
1 2 3 4 5 6 7 8 9 10
'''