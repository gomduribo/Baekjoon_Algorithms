import sys
from itertools import combinations
input=sys.stdin.readline

n=int(input())
chart=[]
total_list=[]
for _ in range(n):
    chart.append(list(map(int,input().split(" "))))
    total_list.append(_)

select_num=int(n/2)
select_team_list=list(combinations(total_list,select_num))
minimum_res=999
for i in range(len(select_team_list)):
    sum1=0
    sum2=0
    result=0
    
    not_select_team_list=[x for x in total_list if x not in select_team_list[i]]
    two_man_list=list(combinations(list(select_team_list[i]),2))
    not_two_man_list=list(combinations(list(not_select_team_list),2))

    for j in range(len(two_man_list)):
        a,b=two_man_list[j]
        sum1=sum1+chart[a][b]+chart[b][a]
    for k in range(len(not_two_man_list)):
        c,d=not_two_man_list[k]
        sum2=sum2+chart[c][d]+chart[d][c]
    if sum1>=sum2:
        result=sum1-sum2
    else:
        result=sum2-sum1
    
    if minimum_res>=result:
        minimum_res=result
print(f"{minimum_res}")