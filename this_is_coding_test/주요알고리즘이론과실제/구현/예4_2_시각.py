import time

n = int(input())

s_time = time.time()

count = 0

for h in range(0,n+1):
    if "3" in str(h):
        count+=3600
        continue
    
    for m in range(0,60):
        if "3" in str(m):
            count+=60
            continue        
        
        for s in range(0,60):
            if "3" in str(s): count+=1

print(count)

e_time = time.time()
print(e_time-s_time)
            