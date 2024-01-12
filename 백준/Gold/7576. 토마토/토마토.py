from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]



def BFS(graph,tomato_list):
  queue=deque(tomato_list)
  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx<0 or nx>=n or ny<0 or ny>=m:
        continue
      if graph[nx][ny]==0:
        graph[nx][ny]=graph[x][y]+1
        queue.append((nx,ny))
      
    

first_line=input().split(" ")
m=int(first_line[0])
n=int(first_line[1])

graph=[]
for i in range(n):
  graph.append(list(map(int, input().split(" "))))

tomato_list=[]
for h in range(n):
  for w in range(m):
    if graph[h][w]==1:
      tomato_list.append((h,w))


BFS(graph,tomato_list)

result=0
for i in graph:
  for j in i:
    if j==0:
      print(-1)
      exit(0)
  result=max(result,max(i))
print(result-1)