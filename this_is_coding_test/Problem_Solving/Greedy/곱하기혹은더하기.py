numbers = input()
result = -1

for i in range(0, len(numbers)):
    cur_num = int(numbers[i])
    if result < 0:
        result = cur_num
        continue

    if cur_num==0 or cur_num==1 or result==0 or result==1:
        result += cur_num

    else:
        result *= cur_num

print(result)