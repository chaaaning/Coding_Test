n, m = map(int, input().split())

max_value = 0

for _ in range(n):
   min_value = min(list(map(int, input().split())))
   if max_value < min_value:
       max_value = min_value

print(max_value)