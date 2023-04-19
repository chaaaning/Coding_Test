import sys
import math

input = sys.stdin.readline

n = int(input())

num_list = [i if i!=0 and i!=1 else 0 for i in range(int(10e6)+1)]

for i in range(2, int(math.sqrt(10e6))+1):
    num = num_list[i]
    if num==0:
        continue
    for j in range(i+i, int(10e6)+1, i):
        num_list[j]=0

answer = 0
for idx in range(n, int(10e6)+1):
    if num_list[idx]==0:
        continue
    elif num_list[idx]//10==0:
        answer = idx
        break
    sp_num = str(num_list[idx])
    num_len = int(math.log10(idx)) + 1
    count = 0
    for k in range(num_len//2+1):
        inv_k = num_len-1-k
        if sp_num[k]==sp_num[inv_k]:
            count+=1
        else:
            break
    if count == num_len//2 + 1:
        answer = idx
        break

print(answer)