n = int(input())
cont = list(map(int, input().split()))

d = [0] * 100
d[0] = cont[0]
d[1] = max(cont[0], cont[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+cont[i])
    
print(d[n-1])