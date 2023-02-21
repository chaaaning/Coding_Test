import sys

input = sys.stdin.readline

letters = input().rstrip()
bomb = input().rstrip()
b_len = len(bomb)
bombs = [bomb[i] for i in range(b_len)]
stack = []
for l in letters:
    stack.append(l)
    if len(stack)<b_len:
        continue
    else:
        if stack[-b_len:] == bombs:
            for _ in range(b_len):
                stack.pop(-1)

if stack:
    print("".join(stack))
else:
    print("FRULA")
    