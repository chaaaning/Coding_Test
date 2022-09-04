import sys

input = sys.stdin.readline

result_list=[]
a, b = map(int, input().split())
while a!=0 and b!=0:
    result_list.append(a+b)
    a, b = map(int, input().split())
for r in result_list:
    print(r)