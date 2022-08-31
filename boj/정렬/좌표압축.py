import sys
import time

input = sys.stdin.readline

n = int(input().rstrip())
numbers = list(map(int, input().split()))

start = time.time()
sorted_numbers = sorted(list(set(numbers)))

index_dict = dict()
for i, num in enumerate(sorted_numbers):
    index_dict[num] = i

for num in numbers:
    print(index_dict[num], end=" ")

print()   
print(time.time()-start)