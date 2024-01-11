from collections import deque

dx=[1,1,1,-1,-1,-1,0,0]
dy=[1,-1,0,-1,1,0,-1,1]
def BFS(graph,h,w):
  width=len(graph[0])
  height=len(graph)
  queue=deque()
  queue.append((h,w))
  graph[h][w]=0
  count=1
  
  while queue:
    y,x=queue.popleft()
    for i in range(8):
      nx=x+dx[i]
      ny=y+dy[i]
      if(nx<0 or nx>=width or ny<0 or ny>=height):
        continue
      if graph[ny][nx]==1:
        # print(f"y:{y} x:{x}")
        # print(f"ny:{ny} nx:{nx}")
        # print(f"graph[1][4]: {graph[1][4]}\n")
        graph[ny][nx]=0
        queue.append((ny,nx))
        count+=1

  return count
  
while True:
  first_line=input().split(" ")
  w=int(first_line[0])
  h=int(first_line[1])
  if w==0 and h==0: break
  
  graph=[]
  for i in range(h):
    graph.append(list(map(int,input().split(" "))))
  
  cnt=[]
  for h_i in range(h):
    for w_i in range(w):
      if graph[h_i][w_i]==1:
        # print(f"h_i w_i:{h_i} {w_i}")
        cnt.append(BFS(graph,h_i,w_i))
  
  print(len(cnt))