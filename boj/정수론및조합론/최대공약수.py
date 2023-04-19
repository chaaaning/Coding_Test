import sys

input = sys.stdin.readline
a, b = map(int, input().split())

# def gcd(n, k):
#     a = max(n, k)
#     b = min(n, k)
#     while a%b!=0:
#         res = a%b
#         a, b = b, res
#     return min(a, b)

def gcd(n, k):
    if k==0:
        return n
    else:
        return gcd(k, n%k)
        
result = gcd(a, b)
while result > 0:
    print(1, end="")
    result-=1