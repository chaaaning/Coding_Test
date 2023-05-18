import sys

input = sys.stdin.readline

n = int(input())
tree_dict = dict()
visited = dict()
for _ in range(n):
    parent, lchild, rchild = input().split()
    tree_dict[parent] = (lchild, rchild)
    visited[parent] = False

def preOrder(node):
    if node==".":
        return None
    print(node, end="")
    preOrder(tree_dict[node][0])
    preOrder(tree_dict[node][1])
    
def postOrder(node):
    if node==".":
        return None
    postOrder(tree_dict[node][0])
    postOrder(tree_dict[node][1])
    print(node, end="")
    
def inOrder(node):
    if node==".":
        return None
    inOrder(tree_dict[node][0])
    print(node, end="")
    inOrder(tree_dict[node][1])
    
preOrder("A")
print()
inOrder("A")
print()
postOrder("A")