import sys
import itertools

input=sys.stdin.readline

N=int(input())
nums=list(map(int,input().split(" ")))
op_list=list(map(int,input().split(" ")))
ops=[]
for i in range(len(op_list)):
  if i==0:
    new=['+']*op_list[i]
    ops=ops+new
  elif i==1:
    new=['-']*op_list[i]
    ops=ops+new
  elif i==2:
    new=['x']*op_list[i]
    ops=ops+new
  elif i==3:
    new=['%']*op_list[i]
    ops=ops+new

# print(ops)
per=list(set(itertools.permutations(ops, N-1)))
results=[]
temp=0
FLAG=0
for p in per:
  temp=0
  for i in range(len(nums)-1):
    FLAG=0
    if i==0:
      temp=nums[i]
      
    if p[i]=="+":
      temp=temp+nums[i+1]
    elif p[i]=="-":
      temp=temp-nums[i+1]
    elif p[i]=="x":
      temp=temp*nums[i+1]
    elif p[i]=="%":
      if temp<0:
        FLAG=1
        temp= -1*temp
      
      temp=temp//nums[i+1]

      if FLAG==1:
        temp= -1*temp
  results.append(temp)

print(max(results))
print(min(results))