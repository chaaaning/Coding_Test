import sys

input = sys.stdin.readline

n, x = map(int, input().split())
arr_a = list(map(int, input().split()))
answer = ""
for val in arr_a:
    if val < x:
        answer += (str(val)+" ")
print(answer)