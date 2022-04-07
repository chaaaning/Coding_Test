import sys
from itertools import combinations as comb

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []*n

def distance(house, chicken):
    return abs((house[0])-(chicken[0]))+abs((house[1])-(chicken[1]))

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
chicken_locs, house_locs = [], []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken_locs.append((i,j))
        elif graph[i][j] == 1:
            house_locs.append((i,j))

available_chicken = list(comb(chicken_locs, m))
chicken_dists = []

for combination in available_chicken:
    total_min = 0
    for house in house_locs:
        min_dist = 102
        for chicken in combination:
            cur_dist = distance(chicken, house)
            if cur_dist < min_dist:
                min_dist = cur_dist
        total_min += min_dist
    chicken_dists.append(total_min)

print(min(chicken_dists))