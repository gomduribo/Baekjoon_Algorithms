import sys
input=sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def BFS(graph,i,j):
    # print("BFS CALLED")
    queue=[]
    queue.append((i,j))
    graph[i][j]=0
    count=1

    while queue:
        x,y=queue.pop(0)
        for j in range(4):
            nx=x+dx[j]
            ny=y+dy[j]
            if nx<0 or nx>=len(graph) or ny<0 or ny>=len(graph[0]):
                continue


            if graph[nx][ny]==1:
                count=count+1
                graph[nx][ny]=0
                queue.append((nx,ny))
    return count
coor_list=[]
for _ in range(int(input())):
    info=str(input()).split(" ")
    M,N,K=int(info[0]),int(info[1]),int(info[2])
    graph=[]
    for _ in range(N):
        graph.append([0]*M)
    for _ in range(K):
        coor=str(input()).split(" ")
        y,x=int(coor[0]),int(coor[1])
        graph[x][y]=1
        coor_list.append((x,y))

    result=[]
    while coor_list:
        cases=coor_list.pop(0)
        if graph[cases[0]][cases[1]]:
            result.append(BFS(graph,cases[0],cases[1]))
    print(len(result))