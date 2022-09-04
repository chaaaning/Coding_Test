import sys
import copy

input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input().rstrip()))

result, rest_money = 0, copy.deepcopy(k)
for i in range(len(coins)-1, -1, -1):
    coin = coins[i]
    if coin > k:
        continue
    else:
        result += rest_money//coin
        rest_money %= coin

print(result)