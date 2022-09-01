import sys

input = sys.stdin.readline

n = int(input().rstrip())
n_set = set(map(int, input().split()))
m = int(input().rstrip())
m_list = list(map(int, input().split()))

for num in m_list:
    if len(set({num})-n_set)==0:
        print(1)
    else:
        print(0)