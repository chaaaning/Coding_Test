# import sys

# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))
# tmp = [0]*n

# def merge_sort(start, end):
#     if end-start < 1: return
#     mid = (start+end)//2
#     merge_sort(start, mid)
#     merge_sort(mid+1, end)
    
#     for i in range(start, end+1):
#         tmp[i] = arr[i]
        
#     k = start
#     idx1, idx2 = start, mid+1
    
#     while idx1<=mid and idx2<=end:
#         if tmp[idx1] < tmp[idx2]:
#             arr[k] = tmp[idx1]
#             k+=1
#             idx1+=1
#         else:
#             arr[k] = tmp[idx2]
#             k+=1
#             idx2+=1
            
#     while idx1<=mid:
#         arr[k] = tmp[idx1]
#         k+=1
#         idx1+=1

#     while idx2<=end:
#         arr[k] = tmp[idx2]
#         k+=1
#         idx2+=1
        
# merge_sort(0, n-1)

# print(arr)

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
tmp = [0]*n

def merge_sort(start, end):
    if end-start < 1: return
    mid = (start+end)//2
    merge_sort(start, mid)
    merge_sort(mid+1, end)
    for i in range(start, end+1):
        tmp[i] = arr[i]
    k = start
    idx1, idx2 = start, mid+1
    # 부분 정렬
    print(start, mid, end)
    while idx1<=mid and idx2<=end:
        print(idx1, idx2, tmp, arr)
        if tmp[idx1] < tmp[idx2]:
            arr[k] = tmp[idx1]
            idx1+=1
            k+=1
        else:
            arr[k] = tmp[idx2]
            idx2+=1
            k+=1
            
    while idx1<=mid:
        arr[k] = tmp[idx1]
        idx1+=1
        k+=1
            
    while idx2<=end:
        arr[k] = tmp[idx2]
        idx2+=1
        k+=1
            
merge_sort(0, n-1)

print(arr)