import sys
import math

input = sys.stdin.readline

a, b = map(int, input().split())

num_list = [i if i!=0 and i!=1 else 0 for i in range(int(math.sqrt(b))+1)]

for i in range(2, int(math.sqrt(b))+1):
    val = num_list[i]
    if val==0:
        continue
    for j in range(i+i, int(math.sqrt(b))+1, i):
        num_list[j]=0

count = 0
for prime_num in num_list:
    if prime_num==0:
        continue
    cur_num = prime_num**2
    sqr_num = 2
    while cur_num <= b:
        if cur_num >= a:
            count+=1
        sqr_num+=1
        cur_num = prime_num**sqr_num
        
print(count)