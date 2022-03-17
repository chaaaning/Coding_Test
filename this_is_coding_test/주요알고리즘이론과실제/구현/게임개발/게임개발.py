n, m = map(int, input().split())

loc_dir = list(map(int, input().split()))
cur_loc, cur_dir  = loc_dir[:2], loc_dir[-1]
count = 1
game_map = []

for _ in range(n):
    game_map.append(list(map(int, input().split())))

game_map[cur_loc[0]][cur_loc[1]] = -1

def check_direction(loc, num):
    if num==0: return [loc[0]-1, loc[1]]
    elif num==1: return [loc[0], loc[1]+1]
    elif num==2: return [loc[0]+1, loc[1]]
    elif num==3: return [loc[0], loc[1]-1]
    return None

while True:
    inner_loop_count = 0
    for i in range(cur_dir, cur_dir-4, -1):
        inner_loop_count+=1
        if cur_dir == i: continue
        can_dir  = i
        if i < 0: can_dir = i+4
        
        can_loc = check_direction(cur_loc, can_dir)
        
        if game_map[can_loc[0]][can_loc[1]] == 0:
            cur_loc = can_loc
            cur_dir = can_dir
            game_map[can_loc[0]][can_loc[1]] = -1
            count+=1
            inner_loop_count-=1
            break
        else:
            continue
    
    if inner_loop_count < 4: continue
    else:
        opp_dir = cur_dir-2 if cur_dir > 1 else cur_dir+2
        opp_loc = check_direction(cur_loc, opp_dir)
        if game_map[opp_loc[0]][opp_loc[1]] == 1:
            break
        else:
            cur_loc = opp_loc

print(count)