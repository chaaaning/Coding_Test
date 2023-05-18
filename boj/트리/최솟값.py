import sys

input=sys.stdin.readline
INF = sys.maxsize
n, m = map(int, input().split())
tree_k, start_idx = 0, 0
while start_idx < n:
    tree_k+=1
    start_idx = 2**tree_k
tree_len = start_idx*2

seg_tree = [INF]*tree_len

def update_min_tree(tree, idx, val):
    tree[idx] = val
    if idx==1:
        return tree
    parent_idx = idx//2
    new_val = min(tree[idx], tree[idx+1]) if idx%2==0 else min(tree[idx-1], tree[idx])
    return update_min_tree(tree, parent_idx, new_val)

def find_min_val(tree, a, b, start_idx=start_idx):
    s, e = start_idx+a-1, start_idx+b-1
    cur_min = sys.maxsize
    while s<=e:
        if s%2==1:
            if cur_min > tree[s]:
                cur_min = tree[s]
            s+=1
        if e%2==0:
            if cur_min > tree[e]:
                cur_min = tree[e]
            e-=1
        s = s//2
        e = e//2
    return cur_min

for i in range(start_idx, start_idx+n):
    seg_tree = update_min_tree(seg_tree, i, int(input()))

result = []
for _ in range(m):
    a, b = map(int, input().split())
    result.append(find_min_val(seg_tree, a, b))
    
for r in result:
    print(r)