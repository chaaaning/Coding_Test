import sys

input = sys.stdin.readline

w, h, x, y, p = map(int, input().split())
r = h//2
left_x, left_y, right_x, right_y = x, y+r, x+w, y+r

def left_circle(ix, iy):
    if (ix-left_x)**2+(iy-left_y)**2 <= r**2: return True
    else: return False
    
def right_circle(ix, iy):
    if (ix-right_x)**2+(iy-right_y)**2 <= r**2: return True
    else: return False
    
def rectangle(ix, iy):
    if (0<= ix-x <= w) and (0 <= iy-y <= h): return True
    else: return False

num_of_players = 0
for _ in range(p):
    new_x, new_y = map(int, input().split())
    if left_circle(new_x, new_y) or right_circle(new_x, new_y) or rectangle(new_x, new_y):
        num_of_players+=1
        
print(num_of_players)