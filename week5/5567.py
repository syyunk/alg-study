from collections import deque


n=int(input())  # 노드의 수
m=int(input())  # 리스트 길이
gr=[[] for _ in range(n+1)]

for i in range(m):
    a, b=map(int, input().split())
    gr[a].append(b)
    gr[b].append(a)

dist=[0]*(n+1)      # 루트노드로부터의 거리 지표
dist[1]=1               # dist[1]=1이라고 시작지점을 초기화해줘야함

def bfs(start):
    q=deque([start])
    while q:
        now=q.popleft()
        for i in gr[now]:
            if not dist[i]:     # 아직 탐색하지 않은 노드면
                dist[i]=dist[now]+1     # 해당 노드의 rn으로부터의 거리=현재 탐색 대상(now)의 rn으로부터의 거리+1
                q.append(i)

bfs(1)
cnt=sum([1 for i in dist if 2<=i<=3])
print(cnt)

