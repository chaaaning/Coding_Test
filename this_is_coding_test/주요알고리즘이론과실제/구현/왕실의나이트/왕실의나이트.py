loc = input()

x, y = ord(loc[0])-96, int(loc[1])
count = 0

dx = [2,2,-2,-2,1,-1,1,-1]
dy = [1,-1,1,-1,2,2,-2,-2]

for idx in range(8):
    move_x = x+dx[idx]
    move_y = y+dy[idx]
    
    if (move_x<1) or (move_x>8) or (move_y<1) or (move_y>8):
        continue
    else: count+=1
    
print(count)