import sys

input = sys.stdin.readline

n, m = map(int, input().split())

basket = [i for i in range(n+1)]

def turn_basket(arr, s, e, m):
    m -= s
    try:
        sub_arr = arr[s:e+1]
        arr[s:e+1] = sub_arr[m:]+sub_arr[:m]
    except:
        sub_arr = arr[s:]
        arr[s:] = sub_arr[m:]+sub_arr[:m]
    return arr

for _ in range(m):
    i, j, k = map(int, input().split())
    basket = turn_basket(basket, i, j, k)

for val in basket[1:]:
    print(val, end=" ")
    

'''
    12345678910
    45612378910
    
'''