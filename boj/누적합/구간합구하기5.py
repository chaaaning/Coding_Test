import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr2D = []
for _ in range(n):
    arr2D.append(list(map(int, input().split())))
    
result = []

for _ in range(m):
    p_result=[]
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1-1, x2):
        p_arr = arr2D[i]
        p_result+=p_arr[y1-1:y2]
    result.append(sum(p_result))
    
for r in result:
    print(r)