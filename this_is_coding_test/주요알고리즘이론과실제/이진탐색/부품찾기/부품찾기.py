def binary_search(arr, start, end, target):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target: return arr[mid]
        elif arr[mid] < target: start = mid+1
        else: end = mid-1
    return None
        
n = int(input())
asemble_list = list(map(int, input().split()))
asemble_list.sort()

m = int(input())
target_list = list(map(int, input().split()))

for target in target_list:
    if binary_search(asemble_list, 0, n-1, target) == target:
        print("yes", end=" ")
    else:
        print("no", end = " ")
