from collections import deque

n, m, v = map(int, input().split())

graph1 = [ [0]*(n+1) for _ in range(n+1) ]
graph2 = [ [0]*(n+1) for _ in range(n+1) ]
visited1 = [0]*(n+1)
visited2 = [0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph1[a][b] = graph1[b][a] = 1
    graph2[a][b] = graph2[b][a] = 1

def DFS(v):
    if visited1[v]:
        return
    visited1[v] = 1
    print(v, end=" ")
    
    for i in range(1, n+1):
        if graph1[v][i] == 1 and (not visited1[i]):
            DFS(i)

def BFS(v):
    queue = deque([v])
    while queue:
        cur = queue.popleft()
        if visited2[cur]:
            continue
        visited2[cur] = 1
        print(cur, end=" ")
        for i in range(1, n+1):
            if graph2[cur][i] == 1 and (not visited2[i]):
                queue.append(i)
                   
DFS(v)
print()
BFS(v)
