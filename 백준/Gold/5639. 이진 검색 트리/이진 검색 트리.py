import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

node_list=[]

while True:
    try:
        node_list.append(int(input()))
    except:
        break

def postorder(first,end):
    if first>end:
        return
    mid=end+1
    for i in range(first+1,end+1):
        if node_list[i]>node_list[first]:
            mid=i
            break
    
    postorder(first+1,mid-1)
    postorder(mid,end)
    print(node_list[first])

postorder(0,len(node_list)-1)