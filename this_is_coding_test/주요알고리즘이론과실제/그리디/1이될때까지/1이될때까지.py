n, k = map(int, input().split())

count = 0

while True:
    count+=1
    count += n%k
    n = n // k
    
    if n < k:
        count+=n-1
        break
    
print(count)