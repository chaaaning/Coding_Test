import sys

input = sys.stdin.readline

n = int(input().rstrip())

def sep_sum(k):
    res_form = k
    for i in range(len(k)):
        res_form=res_form+"+"+k[i]
    return eval(res_form)

initiater = []

for k in range(n-1, n-55, -1): ## 종료 조건을 명확히 할 것
    ans = sep_sum(str(k))
    if ans==n:
        initiater.append(k)
    k-=1

if len(initiater)==0:
    print(0)
else:
    print(initiater[-1])
