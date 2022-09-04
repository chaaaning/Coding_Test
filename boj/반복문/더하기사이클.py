import sys

input = sys.stdin.readline

n = input().rstrip()

count = 0
while True:
    if n=="0":
        count+=1
        break
    if count==0:
        if len(n)==2:
            pre_f, pre_b = n[0], n[1]
        else:
            pre_f, pre_b = "0", n

    b = str(eval(pre_f+"+"+pre_b)%10)
    f = pre_b

    if int(f+b)==int(n):
        count+=1
        break
    else:
        pre_f, pre_b = f, b
        count+=1

print(count)