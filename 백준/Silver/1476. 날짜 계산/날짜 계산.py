import sys
input=sys.stdin.readline

e,s,m=map(int, input().split())

while True:
    if e==s and s==m:
        break
    elif e==min(e,s,m):
        e+=15
    elif s==min(e,s,m):
        s+=28
    elif m==min(e,s,m):
        m+=19
        
        
print(e)