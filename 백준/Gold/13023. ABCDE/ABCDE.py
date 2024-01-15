import sys

def dfs(node, dist):
    global maxdist
    visit[node] = True
    maxdist = max(dist, maxdist)
    if dist >= 4:
        return
    for next_node in graph[node]:
        if visit[next_node] == False:
            dfs(next_node, dist+1)
            visit[next_node] = False

n, m = list(map(int, sys.stdin.readline().split()))
graph = {}
for i in range(n+1):
    graph[i] = []
for i in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    graph[a].append(b)
    graph[b].append(a)


global maxdist
maxdist = -1
check = False
for i in range(0,n+1):
    visit = [False for x in range(n+1)]
    dfs(i, 0)
    if maxdist >= 4:
        print(1)
        check=True
        break
if check == False: print(0)