import sys

input = sys.stdin.readline

n, m = map(int, input().split())
set_s, list_input = set(), []

for _ in range(n):
    set_s.add(input().rstrip())

count = 0
for _ in range(m):
    input_str = input().rstrip()
    if len(set([input_str])-set_s) == 0:
        count+=1
print(count)