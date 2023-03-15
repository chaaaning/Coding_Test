import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
tmp = [0]*n
result = 0

def merge_sort(start, end):
    global result
    if end-start < 1: return
    mid = (start+end)//2
    merge_sort(start, mid)
    merge_sort(mid+1, end)
    
    for i in range(start, end+1):
        tmp[i] = arr[i]
        
    k = start
    idx1, idx2 = start, mid+1
    
    while idx1<=mid and idx2<=end:
        if tmp[idx1] <= tmp[idx2]:
            arr[k]=tmp[idx1]
            k+=1
            idx1+=1
        else:
            result += idx2-k
            arr[k]=tmp[idx2]
            k+=1
            idx2+=1
    while idx1<=mid:
        arr[k]=tmp[idx1]
        k+=1
        idx1+=1
    while idx2<=end:
        arr[k]=tmp[idx2]
        k+=1
        idx2+=1

merge_sort(0, n-1)

print(result)