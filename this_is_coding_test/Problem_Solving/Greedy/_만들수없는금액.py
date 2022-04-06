import sys

input = sys.stdin.readline

n = int(input())
currency = list(map(int, input().split()))
currency.sort()

target = 1
for x in currency:
    if target < x:
        break
    target += x
    print(target)

print(target)