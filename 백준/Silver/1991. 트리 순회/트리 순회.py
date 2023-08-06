import sys
# sys.stdin=open('1991_paik.txt','r')
input=sys.stdin.readline

tree={}

def preorder(node):
    if node!='.':
        print(node,end='')
        preorder(tree[node][0])
        preorder(tree[node][1])

def inorder(node):
    if node!='.':
        inorder(tree[node][0])
        print(node,end='')
        inorder(tree[node][1])  

def postorder(node):
    if node!='.':
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node,end='') 

for _ in range(int(input())):
    nodes=str(input()).split(" ")
    tree[nodes[0]]=[nodes[1],nodes[2][0]]

preorder('A')
print('')
inorder('A')
print('')
postorder('A')