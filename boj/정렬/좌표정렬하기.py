import sys

input = sys.stdin.readline
n = int(input().rstrip())

coordinates = []

for _ in range(n):
    coordinates.append(tuple(map(int, input().split())))
    
coordinates.sort()
for x, y in coordinates:
    print(x, y)