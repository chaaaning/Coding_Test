import sys

input = sys.stdin.readline

n = int(input().rstrip())
stack, result_list = [], []
for _ in range(n):
    command = input().rstrip()
    if "push" in command:
        command, value = command.split()
        value = int(value)
        stack.append(value)
    else:
        if command == "pop":
            try:
                result_list.append(stack.pop(-1))
            except:
                result_list.append(-1)
        elif command == "size":
            result_list.append(len(stack))
        elif command == "empty":
            if len(stack)==0:
                result_list.append(1)
            else:
                result_list.append(0)
        elif command == "top":
            try:
                result_list.append(stack[-1])
            except:
                result_list.append(-1)
                
for result in result_list:
    print(result)