import sys
from collections import deque
from itertools import permutations as perm

input = sys.stdin.readline

bottles = list(map(int, input().split()))
answers = [False]*201
visited = [[False]*201 for _ in range(201)]

search_list = list(perm([0,1,2], 2))

def bfs():
    q = deque([(0,0)])
    visited[0][0]=True
    answers[bottles[2]]=True
    while q:
        a, b = q.popleft()
        c = bottles[2]-a-b
        for s, r in search_list:
            next = [a, b, c]
            total_rs = next[s]+next[r]
            next[r] = total_rs if total_rs<bottles[r] else bottles[r]
            next[s] = total_rs - next[r]
            
            if not visited[next[0]][next[1]]:
                visited[next[0]][next[1]] = True
                q.append((next[0], next[1]))    # 새로 탐색하여 나온 경우임
                if next[0]==0:
                    answers[next[2]] = True

bfs()

for i, val in enumerate(answers):
    if val:
        print(i, end=" ")