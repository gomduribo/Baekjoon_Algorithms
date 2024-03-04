import sys
from collections import deque, defaultdict
import time

input=sys.stdin.readline

visited=[False]*101
def BFS(ladders,snakes):
  q=deque()
  q.append((1,0))
  d_cur=[1,2,3,4,5,6]
  cnt=0
  result=[]
  while q:
    cur=q.popleft()
    if cur[0]==100:
      result.append(cur)
      break
      
    cnt=cur[1]+1
    for i in range(6):
      n_cur=cur[0]+d_cur[i]

      if n_cur>=0 and n_cur<=100:
        new=n_cur
        
        if n_cur in ladders.keys():
          new=ladders[n_cur]
   
        if n_cur in snakes.keys():
          new=snakes[n_cur]
        
        
        if new==100:return cnt

        if not visited[new]:
          visited[new]=True
          q.append((new,cnt))

  return result

N,M=map(int, input().split(" "))
l=defaultdict(int)
s=defaultdict(int)
for _ in range(N):
  x,y=map(int, input().strip().split(" "))
  l[x]=y

for _ in range(M):
  u,v=map(int, input().strip().split(" "))
  s[u]=v
    
print(BFS(l,s))