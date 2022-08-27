import sys

input = sys.stdin.readline
n = int(input().rstrip())
body_list=[]

for _ in range(n):
    w, h = map(int, input().split())
    body_list.append((w, h))

rank_list = []
for std_body in body_list:
    rank = 1
    for i in range(len(body_list)):
        if std_body==body_list[i]:
            continue
        sw, sh = body_list[i]
        if sw>std_body[0] and sh>std_body[1]:
            rank+=1
    rank_list.append(rank)
    
for rank in rank_list:
    print(rank, end=" ")