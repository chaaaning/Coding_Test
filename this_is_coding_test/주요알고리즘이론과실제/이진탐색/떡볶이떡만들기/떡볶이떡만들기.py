n, m = map(int, input().split())
ddeoks = list(map(int,input().split()))

ddeoks.sort()

min_ddeok, max_ddeok = ddeoks[0], ddeoks[-1]

h_list = [x for x in range(min_ddeok, max_ddeok)]

def binary_dsearch(arr, start, end, target, ddeoks):
    
    while start <= end:
        result = 0
        mid = (start+end)//2
        for ddeok in ddeoks:
            if ddeok-arr[mid] >= 0: result+=(ddeok-arr[mid])
        
        if result == target: return arr[mid]
        elif result < target: end = mid-1
        else: start = mid+1
        
    
        
print(binary_dsearch(h_list,0,len(h_list)-1,m,ddeoks))
    