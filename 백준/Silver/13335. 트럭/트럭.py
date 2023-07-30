import sys
input=sys.stdin.readline

n, w, L = map(int,input().split(" "))
trucks=list(map(int,input().split(" ")))
trucks_copy=trucks

bridge=[0]*w

cnt=0
while bridge: 
    cnt=cnt+1
    bridge.pop(0)
    if trucks_copy:
        if sum(bridge)+trucks_copy[0]<=L:
            bridge.append(trucks_copy.pop(0))
        else:
            bridge.append(0)
print(cnt)