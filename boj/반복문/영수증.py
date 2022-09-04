import sys

input = sys.stdin.readline

x = int(input().rstrip())
n = int(input().rstrip())
total_price = 0
for _ in range(n):
    price, num = map(int,input().split())
    total_price+=(price*num)
    
if x-total_price==0: print("Yes")
else: print("No")