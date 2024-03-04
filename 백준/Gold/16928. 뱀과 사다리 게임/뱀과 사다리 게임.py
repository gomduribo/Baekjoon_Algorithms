import sys
from collections import deque, defaultdict
import time

input=sys.stdin.readline

# graph=[list(range(i,i+11)) for i in range(0,91,10) ]
# print(graph)
visited=[False]*101
def BFS(ladders,snakes):
  q=deque()
  q.append((1,0))
  d_cur=[1,2,3,4,5,6]
  cnt=0
  result=[]
  while q:
    # print(f"--{q}")
    cur=q.popleft()
    # time.sleep(0.05)
    # print(cur)
    if cur[0]==100:
      result.append(cur)
      break
      
    # cnt+=1
    cnt=cur[1]+1
    for i in range(6):
      n_cur=cur[0]+d_cur[i]

      if n_cur>=0 and n_cur<=100:
        # print("!!")
        new=n_cur
        # for k in range(len(ladders)):
        #   if ladders[k][0]==n_cur:
        #     # print("ladder!")
        #     new=ladders[k][1]
        #     break
        if n_cur in ladders.keys():
          new=ladders[n_cur]

        # for j in range(len(snakes)):
        #   if snakes[j][0]==n_cur:
        #     # print("snake!")
        #     new=snakes[j][1]
        #     break
        if n_cur in snakes.keys():
          new=snakes[n_cur]
        
        # print(f"-->{(new,cnt)}")
        if new==100:return cnt

        if not visited[new]:
          visited[new]=True
          q.append((new,cnt))

  return result

N,M=map(int, input().split(" "))
l=defaultdict(int)
s=defaultdict(int)
for _ in range(N):
  # l.append(list(map(int, input().strip().split(" "))))
  x,y=map(int, input().strip().split(" "))
  l[x]=y

for _ in range(M):
  u,v=map(int, input().strip().split(" "))
  s[u]=v
# print(l)
print(BFS(l,s))