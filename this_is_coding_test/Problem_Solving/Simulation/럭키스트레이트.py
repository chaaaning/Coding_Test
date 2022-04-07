import sys

input = sys.stdin.readline

n = list(map(int, input().rstrip()))

mid = (len(n)//2)
left, right = n[:mid], n[mid:]
# print(left, right)
if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")