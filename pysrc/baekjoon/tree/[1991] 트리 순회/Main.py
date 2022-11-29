import sys
input = sys.stdin.readline
    
def preorder_travel(data):
    if data != '.':
        print(data, end = "")
        preorder_travel(tree[data][0])
        preorder_travel(tree[data][1])

def inorder_travel(data):
    if data != '.':
        inorder_travel(tree[data][0])
        print(data, end = "")
        inorder_travel(tree[data][1])
        
def postorder_travel(data):
    if data != '.':
        postorder_travel(tree[data][0])
        postorder_travel(tree[data][1])
        print(data, end = "")


n = int(input())
tree = {}

for _ in range(n):
    data, left, right = input().split()
    tree[data] = (left, right)

preorder_travel('A')
print()
inorder_travel('A')
print()
postorder_travel('A')
