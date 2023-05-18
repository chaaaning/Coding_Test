import sys

input=sys.stdin.readline

n, m, k = map(int, input().split())
tree_k, start_idx = 0, 0
stand_num = 1000000007
while start_idx < n:
    tree_k+=1
    start_idx = 2**tree_k

seg_tree = [1]*(2*start_idx)

def update_tree(tree, idx, val, std_num=stand_num):
    tree[idx] = val
    if idx==1:
        return tree
    parent_idx = idx//2
    new_val = tree[idx]*tree[idx+1]%std_num if idx%2==0 else tree[idx-1]*tree[idx]%std_num
    return update_tree(tree, parent_idx, new_val)

def find_prod_val(tree, a, b, start_idx=start_idx, std_num=stand_num):
    s, e = start_idx+a-1, start_idx+b-1
    prod_result = 1
    while s<=e:
        if s%2==1:
            prod_result = prod_result*tree[s]%std_num
            s+=1
        if e%2==0:
            prod_result = prod_result*tree[e]%std_num
            e-=1
        s = s//2
        e = e//2
    return prod_result

for i in range(start_idx, start_idx+n):
    seg_tree[i] = int(input())
 
for i in range(start_idx-1, 0, -1):
    seg_tree[i] = seg_tree[i*2]*seg_tree[i*2+1]%stand_num

result = []
for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a==1:
        seg_tree = update_tree(seg_tree, start_idx+b-1, c)
    else:
        result.append(find_prod_val(seg_tree, b, c))
        
for r in result:
    print(r)