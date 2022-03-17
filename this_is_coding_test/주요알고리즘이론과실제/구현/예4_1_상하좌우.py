import time

n = int(input())
directions = input().split()

start_time = time.time()

cur_loc = (1,1)

def move_R(loc, n):
    target = loc[1]+1
    if (target) < 1 or (target > n): return loc
    else: return (loc[0], loc[1]+1)

def move_L(loc, n):
    target = loc[1]-1
    if (target) < 1 or (target > n): return loc
    else: return (loc[0], loc[1]-1)
        
def move_U(loc, n):
    target = loc[0]-1
    if (target) < 1 or (target > n): return loc
    else: return (loc[0]-1, loc[1])
        
def move_D(loc, n):
    target = loc[0]+1
    if (target) < 1 or (target > n): return loc
    else: return (loc[0]+1, loc[1])

for direction in directions:    
    if direction == "L": cur_loc = move_L(cur_loc, n)
    elif direction == "R": cur_loc = move_R(cur_loc, n)
    elif direction == "U": cur_loc = move_U(cur_loc, n)
    elif direction == "D": cur_loc = move_D(cur_loc, n)

print(cur_loc)

end_time = time.time()
print(f"total time: {end_time-start_time}")

""" 이전 풀이

n = int(input())
plan = list(map(str, input().split()))
start_time = time.time()
direction = {'L':0,'R':1,'U':2,'D':3}
move_x = [-1,1,0,0]
move_y = [0,0,-1,1]

state_y, state_x = 1,1
for moving in plan:
    state_x += move_x[direction[moving]]
    state_y += move_y[direction[moving]]
    if state_x<1 or state_x>n: state_x -= move_x[direction[moving]]
    if state_y<1 or state_y>n: state_y -= move_y[direction[moving]]
print(state_y,' ',state_x)

end_time = time.time()
print(f"total time: {end_time-start_time}")

"""