import sys

input=sys.stdin.readline

n = int(input().rstrip())
value = input().rstrip().rstrip("0")

eval_form_val = ""
for i in range(len(value)):
    eval_form_val = eval_form_val+"+"+value[i]
    
print(eval(eval_form_val))