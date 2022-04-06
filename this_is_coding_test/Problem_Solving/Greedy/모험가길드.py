import sys

input = sys.stdin.readline

n = int(input())
scared_lv = list(map(int, input().split()))

scared_lv.sort(reverse=True)

cur_idx, groups = 0, 0
while len(scared_lv)>cur_idx:
    now = scared_lv[cur_idx]
    cur_idx += now
    groups+=1
    
print(groups)

# hidden이 맞는지에 대한 생각 필요,,

