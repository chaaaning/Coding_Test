import sys

input = sys.stdin.readline

n = int(input().rstrip())
num_list, count_nums = [], dict()
total, min_val, max_val = 0, 4001, -4001
for _ in range(n):
    input_num = int(input().rstrip())
    total+=input_num    # Total
    
    if input_num < min_val: # min
        min_val = input_num
    if input_num > max_val:
        max_val = input_num # max
        
    num_list.append(input_num) # sort
    try:
        count_nums[input_num]+=1
    except:
        count_nums[input_num] = 1

num_list.sort()
sorted_key = list(map(lambda x: (x,count_nums[x]),sorted(count_nums)))
sorted_key_value = sorted(sorted_key, key=lambda x: x[1],reverse=True)

print(round(total/n))
print(num_list[n//2])
if n!=1:
    if count_nums[sorted_key_value[0][0]]!=count_nums[sorted_key_value[1][0]]:
        print(sorted_key_value[0][0])
    else:
        print(sorted_key_value[1][0])
else:
    print(num_list[0])
print(max_val-min_val)

# print()
# print(f"AVG: {round(total/n)}")
# print(f"MED: {num_list[n//2]}")
# print(f"MAN: {sorted_key_value[0]}")
# print(f"RAN: {max_val-min_val}")