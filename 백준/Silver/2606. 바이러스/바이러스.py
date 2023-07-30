import sys
input = sys.stdin.readline

def DFS(node,count):
    visited[node]=1
    for adj_node in graph[node]:
        if visited[adj_node]==0:
            count=DFS(adj_node,count=count+1)
    return count

num_com=int(input())
num_connect=int(input())
# print(f"--{num_com}, {num_connect}")

graph=[[] for _ in range(num_com+1)]
visited=[0]*(num_com+1)

for _ in range(num_connect):
    a,b=map(int,input().split(" "))
    graph[a].append(b)
    graph[b].append(a)
# print(graph)
print(DFS(1,0))