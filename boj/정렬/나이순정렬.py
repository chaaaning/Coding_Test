import sys

input = sys.stdin.readline

n = int(input().rstrip())

clients = []

for i in range(n):
    age, name = map(str, input().split())
    clients.append((int(age), i, name))
    
clients.sort()

for age, rank, name in clients:
    print(age, name)