from collections import deque
from operator import truediv


n,m,start=map(int,input().split())
visited=[False]*(n+1)

gr=[[] for _ in range(n+1)]

for _ in range(m):
    a, b=map(int, input().split())
    gr[a].append(b)
    gr[b].append(a)

for i in range(len(gr)):
    gr[i].sort()

def dfs(start):
    print(start, end=' ')
    visited[start]=True
    for i in gr[start]:
        if not visited[i]:
            dfs(i)      # 방문을 진행
            visited[i]=True

def bfs(start):
    q=deque([start])
    visited[start]=True
    while q:
        now=q.popleft()
        print(now, end=' ')
        for i in gr[now]:
            if not visited[i]:
                q.append(i)
                visited[i]=True

dfs(start)
visited=[False]*(n+1)
print()
bfs(start)
