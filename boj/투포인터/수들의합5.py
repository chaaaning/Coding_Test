import sys

input = sys.stdin.readline

n = int(input())

sum_val, ans, start_idx, end_idx = 1, 1, 1, 1

while start_idx < n:
    if sum_val > n:
        sum_val-=start_idx
        start_idx+=1
    elif sum_val < n:
        end_idx+=1
        sum_val+=end_idx
    else:
        ans+=1
        end_idx+=1
        sum_val+=end_idx
        
print(ans)
    
# for s in range(1,n+1):
#     p_sum = 0
#     for i in range(s, n+1):
#         p_sum+=i
#         if p_sum==n:
#             ans+=1
#             break
#         elif p_sum>n:
#             break
#         else:
#             continue

