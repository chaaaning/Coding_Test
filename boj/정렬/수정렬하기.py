import sys

input=sys.stdin.readline

n = int(input().rstrip())

num_list = []
for _ in range(n):
    num_list.append(int(input().rstrip()))
    
num_list.sort()

for num in num_list:
    print(num)