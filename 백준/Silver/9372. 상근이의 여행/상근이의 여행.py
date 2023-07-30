import sys
input = sys.stdin.readline

case_num = int(input())

def DFS(v,count):
    # print("DFS CALLED")
    visited[v]=1
    
    for adj in graph[v]:
        if visited[adj]==0:
            # count=count+1
            count=DFS(adj,count+1)
    return count


for i in range(case_num):
    case=str(input())
    country_num=int(case.split(" ")[0])
    plane_num=int(case.split(" ")[1])
    graph=[[] for _ in range(country_num+1)]
    visited=[0]*(country_num+1)
    
    for j in range(plane_num):
        a,b=map(int, input().split(" "))
        graph[a].append(b)
        graph[b].append(a)
            
    # print(graph)
    print(DFS(1,0))
    # print("----------")