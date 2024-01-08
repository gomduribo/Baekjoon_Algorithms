import sys
input=sys.stdin.readline

def merge_sort(arr):
    if(len(arr)<2):
        return arr
    mid=len(arr)//2
    low_arr=merge_sort(arr[:mid])
    high_arr=merge_sort(arr[mid:])
    
    l=h=0
    total_arr=[]
    
    while(l<len(low_arr) and h<len(high_arr)):
        if(low_arr[l]<high_arr[h]):
            total_arr.append(low_arr[l])
            l+=1
        else:
            total_arr.append(high_arr[h])
            h+=1
    total_arr=total_arr+low_arr[l:]
    total_arr=total_arr+high_arr[h:]
    return total_arr

num=int(input())
total_list=[]
for i in range(num):
    total_list.append(int(input()))

total_arr=merge_sort(total_list)
for j in range(len(total_arr)):
    print(total_arr[j])
