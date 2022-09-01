import sys

input = sys.stdin.readline

n = int(input().rstrip())
first_numbers = set(map(int, input().split()))
m = int(input().rstrip())
second_numbers = list(map(int, input().split()))

for num in second_numbers:
    number = set([num]).intersection(first_numbers)
    print(len(number), end=" ")