import sys

input = sys.stdin.readline

n = int(input())

meetings = []

for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))
    
meetings.sort()
meetings = sorted(meetings, key = lambda x: x[1])

pre_last = 0
total = 0
for p_start, p_end in meetings:
    if p_start >= pre_last:
        total+=1
        pre_last = p_end

print(total)

'''
    해당 문제의 힌트는 Greedy 라는 것.
    브루트포스로 문제를 풀 수 있지만, greedy 관점에서 정렬 순서를 잘 맞추면 됨
    간단히 풀 수 있는 것을 완전 탐색으로만 아이디어를 떠올리는 문제.
'''