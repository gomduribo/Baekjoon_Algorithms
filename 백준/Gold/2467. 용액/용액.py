import sys
input=sys.stdin.readline

N=int(input())
nums=list(map(int,input().split(' ')))

start,end=0,len(nums)-1
record=[abs(nums[start]+nums[end]),0,len(nums)-1]
while start<end:
    two_sum=nums[start]+nums[end]
    if abs(two_sum)<record[0]:
        record=[abs(two_sum),start,end]

        if record[0]==0:
            break
    
    if two_sum<0:
        start=start+1
    else:
        end=end-1
print(nums[record[1]],nums[record[2]])