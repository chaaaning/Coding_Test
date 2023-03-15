# # 기수정렬을 이용한 풀이
# import sys
# from collections import deque
# from copy import deepcopy as dcopy

# input = sys.stdin.readline

# max_len = 0
# input_lst = []

# n = int(input())
# for _ in range(n):
#     a = input().rstrip()
#     a_len = len(a)
#     if a_len > max_len:
#         max_len=a_len
#     input_lst.append(a)

# digit_q = [deque([]) for _ in range(10)]
# for val in input_lst:
#     digit_q[int(val[-1])].append("0"*(max_len-len(val))+val)


# for i in range(max_len-2, -1, -1):
#     new_q = [deque([]) for _ in range(10)]
#     for n in range(0,10):
#         cur_q = digit_q[n]
#         while cur_q:
#             cur_num = cur_q.popleft()
#             idx = int(cur_num[i])
#             new_q[idx].append(cur_num)
#     digit_q = dcopy(new_q)
    
# for i in range(9,-1,-1):
#     while digit_q[i]:
#         print(int(digit_q[i].pop()))

import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

s_arr = sorted(arr, reverse=True)

for v in s_arr:
    print(v)
