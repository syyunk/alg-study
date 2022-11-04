import sys
from collections import deque
input=sys.stdin.readline

node, edge, start=map(int, input().split())
gr=[[] for _ in range(node+1)]

for _ in range(edge):
    a, b=map(int, input().split())
    gr[a].append(b)
    gr[b].append(a)

for i in range(len(gr)):
    gr[i].sort()

visited=[False]*(node+1)
def dfs(start):
    visited[start]=True
    print(start, end=' ')
    for i in gr[start]:
        if not visited[i]:
            dfs(i)
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
visited=[False]*(node+1)
print()
bfs(start)