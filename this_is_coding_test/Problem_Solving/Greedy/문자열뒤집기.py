import sys

input = sys.stdin.readline

n = input()

interval_split = [0, 0]
std_value = n[0]

for i in range(0, len(n)):
    if std_value != n[i]:
        interval_split[int(std_value)]+=1
        std_value = n[i]
        
print(min(interval_split))