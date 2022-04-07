import sys
from collections import deque

INF = int(1e9)
input = sys.stdin.readline

n = int(input().rstrip())   # Board Size (n head_x n board)
k = int(input().rstrip())   # The number of apples
board = [[0]*(n+1) for _ in range(n+1)]     # define board

for _ in range(k):                          # ehead_xpression about location of apples
    a, b = map(int, input().split())
    board[a][b] = 1
    
l = int(input().rstrip())    # The number of transformation directions

head_loc = (1,1)
board[1][1] = -1
cur_direction = "R"
head_direction = {
    "U":{"L":(0,-1,"L"), "D":(0,1,"R"), "S":(-1,0)},
    "D":{"L":(0,1,"R"), "D":(0,-1,"L"), "S":(1,0)},
    "L":{"L":(1,0,"D"), "D":(-1,0,"U"), "S":(0,-1)},
    "R":{"L":(-1,0,"U"),"D":(1,0,"D"), "S":(0,1)}
    }
direction_list = []

for _ in range(l):
    head_x, c = map(str, input().split())
    direction_list.append((int(head_x),c))
direction_list.append((INF,"Z"))

time = 0
q = deque([head_loc])
while True:
    time+=1
    if time <= direction_list[0][0]:
        head_x, head_y = head_loc[0]+head_direction[cur_direction]["S"][0], head_loc[1]+head_direction[cur_direction]["S"][1]
        
        if head_x<1 or head_y<1 or head_x>n or head_y>n or board[head_x][head_y]==-1:
            break
        elif board[head_x][head_y] == 0:
            tail_x, tail_y = q.popleft()
            q.append((head_x, head_y))
            board[head_x][head_y] = -1
            board[tail_x][tail_y] = 0
        elif board[head_x][head_y] == 1:
            board[head_x][head_y] = -1
            q.append((head_x, head_y))
            
        head_loc = (head_x,head_y)
        
    else:
        dir = direction_list.pop(0)[1]
        head_x, head_y = head_loc[0]+head_direction[cur_direction][dir][0], head_loc[1]+head_direction[cur_direction][dir][1]
        cur_direction = head_direction[cur_direction][dir][2]
        
        if head_x<1 or head_y<1 or head_x>n or head_y>n or board[head_x][head_y]==-1:
            break
        elif board[head_x][head_y] == 0:
            tail_x, tail_y = q.popleft()
            q.append((head_x, head_y))
            board[head_x][head_y] = -1
            board[tail_x][tail_y] = 0
        elif board[head_x][head_y] == 1:
            board[head_x][head_y] = -1
            q.append((head_x, head_y))
            
        head_loc = (head_x,head_y)
        
print(time)

"""
복잡하게 구현할 필요가 없다.

대신 구현에서 원하는 바를 정확히 파악해야 한다. 나는 아직 방향에 대한 구현에 있어서 딕셔너리로 구현하는 것이 편하나,
책에서의 경우 방향에 대한 구현을 리스트로 정의하고, 리스트의 인덱스로 접근한다. 이는 구현에 대한 문제를 많이 풀어 보면서
현재 방식에 익숙해 지거나, 리스트 인덱스 접근 방식을 습득하는 것 둘 중 하나의 방향성을 설정하고 시간을 단축하는 것이 필요하다.

    1. 구현에서 원하는 동작을 제대로 파악할 것
    2. 구현 문제에서 나만의 솔루션을 익히고, 빠르게 적용할 것
"""