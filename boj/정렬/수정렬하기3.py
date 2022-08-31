import sys

input=sys.stdin.readline

n = int(input().rstrip())
count_table = [0]*10001

for _ in range(n):
    count_table[int(input().rstrip())] += 1

for i in range(0, 10001):
    if count_table[i]==0:
        continue
    for _ in range(count_table[i]):
        print(i)