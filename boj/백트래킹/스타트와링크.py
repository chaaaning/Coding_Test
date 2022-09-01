import sys
from itertools import combinations as comb

input = sys.stdin.readline

n = int(input().rstrip())
ability_table = []

for _ in range(n):
    ability_table.append(list(map(int, input().split())))

case_list = [i for i in range(n)]

start_team = list(comb(case_list, n//2))
link_team = list(map(lambda x: tuple(set(case_list)-set(x)), start_team))

min_ability_diff = int(1e9)

for s_ab, l_ab in zip(start_team, link_team):
    start_ability, link_ability = 0, 0
    for (i,j),(k,l) in zip(comb(s_ab,2), comb(l_ab,2)):
        start_ability = start_ability + ability_table[i][j] + ability_table[j][i]
        link_ability = link_ability + ability_table[k][l] + ability_table[l][k]
        
    ability_diff = abs(start_ability-link_ability)
    if ability_diff < min_ability_diff:
        min_ability_diff = ability_diff
print(min_ability_diff)