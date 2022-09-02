import sys

input = sys.stdin.readline

n = int(input().rstrip())
num_list = list(map(int, input().split()))

stk, result_list = [], [-1]*n
for i,num in enumerate(num_list):
    if not stk:
        stk.append((num, i))
    else:
        if stk[-1][0] > num:
            stk.append((num, i))
        else:
            while True:
                if stk[-1][0] < num:
                    idx = stk.pop(-1)[1]
                    result_list[idx] = num
                    if not stk:
                        stk.append((num, i))
                        break
                else:
                    stk.append((num, i))
                    break
for result in result_list:
    print(result, end=" ")