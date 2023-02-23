import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans, ia, ib = 0, 0, n-1

while ia < ib:
    S = arr[ia] + arr[ib]
    if S > m: ib-=1
    elif S < m: ia+=1
    else:
        ib-=1
        ia+=1
        ans+=1
        
print(ans)