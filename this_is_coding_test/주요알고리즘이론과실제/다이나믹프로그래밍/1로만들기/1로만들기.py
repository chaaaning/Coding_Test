x = int(input())

d = [0] * (x+1)
inf = 1e9

for i in range(2, x+1):
    c5, c3, c2 = inf, inf, inf
    if i % 5 == 0:
        c5 = d[i//5] + 1
    if i % 3  == 0:
        c3 = d[i//3] + 1
    if i % 2 == 0:
        c2 = d[i//2] + 1
    d[i] = min(c5, c3, c2, d[i-1]+1)

print(d[x])