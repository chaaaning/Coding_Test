import sys

input = sys.stdin.readline

n = int(input().rstrip())
times = list(map(int, input().split()))
times.sort()

total_times = [sum(times[0:i]) for i in range(1, n+1)]
print(sum(total_times))