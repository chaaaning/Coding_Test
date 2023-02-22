import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr2D = [[0]*(n+1)]
for _ in range(n):
    p_input = [0] + list(map(int, input().split()))
    arr2D.append(p_input)
    
    
result = []

for _ in range(m):
    p_result=0
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2+1):
        p_arr = arr2D[i]
        p_result += sum(p_arr[y1:y2+1])
    result.append(p_result)
    
for r in result:
    print(r)
    
# for i in range(n+1):
#     print(arr2D[i])
'''
    pypy3 통과
'''