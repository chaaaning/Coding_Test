import sys

input = sys.stdin.readline
s = input().rstrip()
result_set = set()
for i in range(len(s)):
    for j in range(len(s)):
        result_set.add(s[j:j+i])
print(len(result_set))