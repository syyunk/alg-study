
import sys
sys.setrecursionlimit(10000)

n, m=map(int, sys.stdin.readline().split())
visited=[False]*(n+1)
gr=[[]for _ in range(n+1)]
cnt=0

for _ in range(m):
    u, v=map(int, sys.stdin.readline().split())
    gr[u].append(v)
    gr[v].append(u)


def dfs(start):
    visited[start]=True
    for i in gr[start]:     # 시작점을 기준으로 탐색
        if not visited[i]:
            dfs(i)      # 방문을 진행
            visited[i]=True



for i in range(1, n+1):
    if not visited[i]:
        if not gr[i]:       # 해당 정점 i에 연결된 그래프가 없다면
            cnt+=1
            visited[i]=True
        else:               # 연결된 그래프가 있다면 dfs탐색
            dfs(i)
            visited[i]=True

            cnt+=1

print(cnt)

