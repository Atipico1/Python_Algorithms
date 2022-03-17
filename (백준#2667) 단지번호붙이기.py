import sys
n = int(sys.stdin.readline())
L = [list(map(int, list(input()))) for _ in range(n)]
visited = [ [0]*n for _ in range(n) ]
cnt = 0
result = []
a = 0
def DFS(x, y):
    global a
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    if visited[x][y]:
        return
    if L[x][y] == 1:
        visited[x][y] = 1
        a += 1
        DFS(x+1, y)
        DFS(x-1, y)
        DFS(x, y+1)
        DFS(x, y-1)
        
for i in range(n):
    for j in range(n):
        if L[i][j] == 1 and (not visited[i][j]):
            a = 0
            DFS(i, j)
            cnt += 1
            result.append(a)

print(cnt)
result.sort()
for i in result:
    print(i)
