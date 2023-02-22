import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr_s, total, ans = [], 0, 0
rest_list = [0]*m

for a in arr:
    total+=a
    rest = total%m
    if rest==0:
        ans+=1
    rest_list[rest]+=1
    arr_s.append(rest)

for val in rest_list:
    ans+=val*(val-1)//2    

print(ans)