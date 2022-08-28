import sys

input = sys.stdin.readline
n, m = map(int, input().split())
chess_board = []

for _ in range(n):
    board_row = input().rstrip()
    chess_board.append(list(map(lambda x: 1 if x=="W" else -1, board_row)))
    
w_board = [[1,-1]*4 if i%2==0 else [-1,1]*4 for i in range(8)]
b_board = [[-1,1]*4 if i%2==0 else [1,-1]*4 for i in range(8)]

def list_diff(l1,l2):
    return list(map(lambda x,y: abs(y-x)//2, l1,l2))

diff_n, diff_m, min_num = n-7, m-7, int(1e9)
for i in range(0,diff_n):
    for j in range(0,diff_m):
        partial_chb = [chb[j:j+8] for chb in chess_board[i:i+8]]

        w_result = sum(list(map(lambda r1,r2: sum(list_diff(r1,r2)), partial_chb, w_board)))
        b_result = sum(list(map(lambda r1,r2: sum(list_diff(r1,r2)), partial_chb, b_board)))
        partial_min = min(w_result, b_result)
        
        if min_num>partial_min:
            min_num=partial_min
print(min_num)