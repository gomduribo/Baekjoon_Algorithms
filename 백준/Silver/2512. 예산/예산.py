import sys
input=sys.stdin.readline

N=int(input())
budgets=list(map(int,input().split(" ")))
total_budget=int(input())
total=0
start,end=0,max(budgets)

total_rec=[]

while start<=end:
    total=0
    mid=int((start+end)/2)
    for bud in budgets:
        if bud>=mid:
            total=total+mid
        else:
            total=total+bud
    if total>total_budget:
        end=mid-1
    elif total<=total_budget:
        start=mid+1
    # print(f"total, limit:{total}, {mid}")
print(f'{end}')
