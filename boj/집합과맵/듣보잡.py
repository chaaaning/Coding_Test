import sys

input = sys.stdin.readline

n, m = map(int, input().split())

not_listen, not_see = set(), set()

for _ in range(n):
    not_listen.add(input().rstrip())
    
for _ in range(m):
    not_see.add(input().rstrip())

not_see_listen = not_listen.intersection(not_see)
print(len(not_see_listen))

not_see_listen_list = list(not_see_listen)
not_see_listen_list.sort()
for name in not_see_listen_list:
    print(name)