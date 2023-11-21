from collections import deque

def solution(queue1, queue2):
    queue1=deque(queue1)
    queue2=deque(queue2)
    s1=sum(queue1)
    s2=sum(queue2)
    total=s1+s2
    length=len(queue1)+len(queue2)
    lim=len(queue1)*3
    target=total/2
    if total%2==1:
        return -1
    
    count=0
    while(True):
        if(s1>s2):
            i=queue1.popleft()
            queue2.append(i)
            s1=s1-i
            s2=s2+i
            count=count+1
        elif(s2>s1):
            i=queue2.popleft()
            queue1.append(i)
            s1=s1+i
            s2=s2-i
            count=count+1
        else:break
        
        if count==lim: return -1
    answer = count
    print(answer)
    return answer