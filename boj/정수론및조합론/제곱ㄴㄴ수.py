import sys
import math

input = sys.stdin.readline

mn, mx = map(int, input().split())
check_list = [1] * (mx-mn+1)

for i in range(2, int(math.sqrt(mx))+1):
    pow = i**2
    start_idx = mn//pow
    if mn%pow!=0:
        start_idx+=1
    for j in range(start_idx, (mx//pow)+1):
        check_list[int(j*pow)-mn]=0
        
print(sum(check_list))