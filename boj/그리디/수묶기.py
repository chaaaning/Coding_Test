import sys

input = sys.stdin.readline

n = int(input())

zero_num = 0
u_zero, o_zero = [], []

for _ in range(n):
    val = int(input())
    if val==0:
        zero_num += 1
    elif val > 0:
        o_zero.append(val)
    else:
        u_zero.append(val)
        
o_zero.sort(reverse=True)
u_zero.sort()

answer = 0
for i in range(0, len(u_zero)):
    if i%2==0 and i==len(u_zero)-1:
        num = u_zero[i]
        if zero_num!=0:
            zero_num-=1
            break
        else:
            answer+=num
    else:
        if i%2==1:
            continue
        num1, num2 = u_zero[i], u_zero[i+1]
        answer+=(num1*num2)

for i in range(0, len(o_zero)):
    if i%2==0 and i==len(o_zero)-1:
        answer += o_zero[i]
    else:
        if i%2==1:
            continue
        num1, num2 = o_zero[i], o_zero[i+1]
        if num1==1 or num2==1:
            answer += (num1+num2)
        else:
            answer+=(num1*num2)
print(answer)