import sys

input = sys.stdin.readline

n = int(input())
line_num = 2*n-1

storage = []
for i in range(1, n+1):
    res = " "*(n-i)+"*"*(2*i-1)
    print(" "*(n-i)+"*"*(2*i-1))
    storage.append(res)
    
for i in range(1,n):
    print(storage[-i-1])