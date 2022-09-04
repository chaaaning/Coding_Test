import sys

input = sys.stdin.readline

n = int(input().rstrip())

directions = [[] for _ in range(5)]
input_sequence = []

for i in range(6):
    direction, length = map(int, input().split())
    directions[direction].append((i, length))
    input_sequence.append(length)

max_idx_list, total = [], 1
for i in range(1,5):
    if len(directions[i]) == 1:
        idx, length = directions[i][0]
        total*=length
        max_idx_list.append(idx)
        
if abs(max_idx_list[1]-max_idx_list[0])==1:
    max_idx=max(max_idx_list)
else:
    max_idx=min(max_idx_list)

try:
    a, b = input_sequence[max_idx+2], input_sequence[max_idx+3]
except:
    a, b = input_sequence[max_idx-4], input_sequence[max_idx-3]
    
result = total-(a*b)
print(n*result)