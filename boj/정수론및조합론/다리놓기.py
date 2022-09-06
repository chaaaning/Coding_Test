import sys
import math
input = sys.stdin.readline

test_num = int(input().rstrip())

def bicomb(n, k):
    return(math.factorial(n)//(math.factorial(k)*math.factorial(n-k)))
result_list = []
for _ in range(test_num):
    a, b = map(int, input().split())
    result_list.append(bicomb(b, b-a))
    
for result in result_list:
    print(result)