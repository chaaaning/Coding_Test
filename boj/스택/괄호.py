import sys

input = sys.stdin.readline

n = int(input().rstrip())
result_list = []

def is_vps(letters):
    stk = []
    for l in letters:
        if len(stk) == 0:
            stk.append(l)
        else:
            if l=="(":
                stk.append(l)
            else:
                if stk[-1]=="(":
                    stk.pop(-1)
                else:
                    stk.append(l)
    if len(stk)==0:
        return "YES"
    else:
        return "NO"
    
for _ in range(n):
    input_letter = input().rstrip()
    result_list.append(is_vps(input_letter))

for result in result_list:
    print(result)