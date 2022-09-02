import sys

input = sys.stdin.readline

n = int(input().rstrip())

result_list, stk, arr, pop_list = ["+"], [1], [], []
for _ in range(n):
    inum = int(input().rstrip())
    arr.append(inum)

target_index, increase_num = 0, 2
while stk or increase_num<=n:
    try:
        target_num = arr[target_index]
    except:
        pass
    if len(stk)!=0:
        if target_num==stk[-1] or increase_num>n:
            pop_list.append(stk.pop(-1))
            result_list.append("-")
            target_index+=1
        else:
            stk.append(increase_num)
            result_list.append("+")
            increase_num+=1
    else:
        stk.append(increase_num)
        result_list.append("+")
        increase_num+=1

if sum(list(map(lambda x,y: 0 if x==y else 1, arr, pop_list)))!=0:
    print("NO")
else:
    for result in result_list:
        print(result)