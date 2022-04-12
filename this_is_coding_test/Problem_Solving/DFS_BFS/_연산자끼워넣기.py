# import sys
# import math

# from sympy import frac

# input = sys.stdin.readline

# n = int(input().rstrip())
# num_list = list(map(str, input().split()))
# opers = list(map(int, input().split()))     # +, -, *, /
# oper_name = ["+", "-", "*", "//"]

# result = []

# def case_num(opers, n):
#     total_n = n-1
#     total_opr = sum(opers)
#     fac = math.factorial(n-1)
#     frac_bottom = 1
#     for i in opers:
#         if i!=0:
#             frac_bottom *= i
#     return fac//frac_bottom

# total_oper_num = case_num(opers, n)

# def find_oper(num_list, result, opers, res):
#     if sum(opers)==0:
#         return None
    
#     if res==0:
#         res = num_list.pop(0)
#         a = num_list.pop(0)
#     else:
#         a = num_list.pop(0)
    
#     print(f"res: {res}\ta: {a}")
        
#     for i in range(4):
#         if opers[i]==0:
#             continue
#         res = eval(str(res)+oper_name[i]+a)
#         opers[i]-=1
#         print("--recurcive start--")
#         find_oper(num_list, result, opers, res)
#         print("--recurcive end--")
#         print(f"num_list: {num_list}, result: {result}, opers: {opers}")
#         print()
#         if sum(opers)==0:
#             result.append(res)
            
#     if len(result)==total_oper_num:
#         return result
    
# print(find_oper(num_list, result, opers, 0))


import sys

input = sys.stdin.readline

n = int(input().rstrip())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())      # 연산자의 개수

min_val = 1e9
max_val = -1e9

def dfs(i, now):
    global min_val, max_val, add, sub, mul, div
    if i==n:
        min_val = min(min_val, now)
        max_val = max(max_val, now)
    else:
        if add > 0:
            add-=1
            dfs(i+1, now+data[i])
            add+=1
        if sub > 0:
            sub-=1
            dfs(i+1, now-data[i])
            sub+=1
        if mul > 0:
            mul-=1
            dfs(i+1, now*data[i])
            mul+=1
        if div > 0 :
            div-=1
            dfs(i+1, int(now/data[i]))
            div+=1

dfs(1, data[0])

print(max_val)
print(min_val)


"""
real DIFFICULT!!
단순히 생각하면 연산자 경우의 수 완전 탐색을 해도 될 정도의 여유가 있지만,
문제를 제시한 section이 BFS/DFS 인 것을 고려하여 문제를 접근했기에 DFS의 Recursive의
원리로 탐색을 진행하려 했다. 해당 경우의 DFS 알고리즘 적용 방식은 기존의 graph를 통한 방식과
다르기 때문에 쉽게 생각하는 것이 어려웠다. 비록 틀렸지만, 이번에 확실히 익히고 DFS의 활용범위를
넓혀 나가는 사고를 기르도록 하자.
---
    <Main Point>
        1. global 선언으로 재귀 어느 단계에서도 변하지 않는 변수 생성
        2. 재귀 step이 행해지는 부분에 대한 구현
"""