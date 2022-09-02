import sys

input = sys.stdin.readline

def is_vps(letters):
    stk = []
    for l in letters:
        if len(stk) == 0:
            stk.append(l)
        else:
            if l=="(" or l=="[":
                stk.append(l)
            elif l==")":
                if stk[-1]=="(":
                    stk.pop(-1)
                else:
                    stk.append(l)
            else:
                if stk[-1]=="[":
                    stk.pop(-1)
                else:
                    stk.append(l)
    if len(stk)==0:
        return "yes"
    else:
        return "no"
result_list = []
while True:
    sts = input().rstrip()
    if sts==".":
        break
    stk_input_s = ""
    for s in sts:
        if s=="(" or s=="[" or s==")" or s=="]":
            stk_input_s+=s
    result_list.append(is_vps(stk_input_s))

for result in result_list:
    print(result)