import sys

input = sys.stdin.readline
n = int(input().rstrip())

coordinates = []

for _ in range(n):
    x, y = map(int, input().split())
    coordinates.append((y, x))
    
coordinates.sort()
for y, x in coordinates:
    print(x, y)