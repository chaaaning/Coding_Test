import sys

input = sys.stdin.readline

test_num = int(input().rstrip())

def is_in_cir(cx, cy, r, ix, iy):
    if (ix-cx)**2+(iy-cy)**2 <= r**2: return True
    else: return False

result_list = []

for _ in range(test_num):
    start_x, start_y, end_x, end_y = map(int, input().split())
    num_circles = int(input().rstrip())
    start_num, end_num = 0, 0
    for _ in range(num_circles):
        c_x, c_y, r = map(int, input().split())
        if is_in_cir(c_x, c_y, r, start_x, start_y) and is_in_cir(c_x, c_y, r, end_x, end_y): continue
        elif is_in_cir(c_x, c_y, r, end_x, end_y): end_num+=1
        elif is_in_cir(c_x, c_y, r, start_x, start_y): start_num+=1
    result_list.append(start_num+end_num)

for result in result_list:
    print(result)