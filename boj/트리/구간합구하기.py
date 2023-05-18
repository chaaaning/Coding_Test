import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
tree_k = 0
start_idx = 0
while start_idx < n:
    tree_k+=1
    start_idx = 2**tree_k
    
binary_tree = [0]*(2*start_idx)
for i in range(start_idx, start_idx+n):
    binary_tree[i] = int(input())
    
for i in range(start_idx-1, 0, -1):
    lchild_index, rchild_index = i*2, i*2+1
    binary_tree[i] = binary_tree[lchild_index]+binary_tree[rchild_index]

def update_tree(tree, idx, val):
    tree[idx] = val
    if idx==1:
        return tree
    parent_node = idx//2
    new_val = tree[idx]+tree[idx+1] if idx%2==0 else tree[idx-1]+tree[idx]
    return update_tree(tree, parent_node, new_val)

partial_sum = []
for _ in range(m+k):
    a, b, c = map(int, input().split())
    s=start_idx+b-1
    e=(c-b)+s
    if a==1:
        new_tree = update_tree(binary_tree, s, c)
    else:
        sum_node = 0
        while s<=e:
            if s%2==1:
                sum_node+=binary_tree[s]
                s+=1
            if e%2==0:
                sum_node+=binary_tree[e]
                e-=1
            s = s//2
            e = e//2
        partial_sum.append(sum_node)
            
for r in partial_sum:
    print(r)