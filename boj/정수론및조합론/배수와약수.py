import sys

input = sys.stdin.readline
result_list = []
while True:
    max_val, min_val = 0, 0
    a, b = map(int, input().split())
    if a==0 and b==0: break
    if a>b:
        if a%b==0: result_list.append("multiple")
        else: result_list.append("neither")
    elif a<b:
        if b%a==0: result_list.append("factor")
        else: result_list.append("neither")
        
for result in result_list:
    print(result)