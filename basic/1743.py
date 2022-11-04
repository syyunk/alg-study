#그래프 입력받는 방식을 2667과 비교 - trash[x][y] 초기 방문처리하는 위치..
import sys
from collections import deque

input=sys.stdin.readline

dx=[0, 0, -1, 1]
dy=[1, -1, 0, 0]

def bfs(trash, a, b):
    q=deque()
    q.append([a, b])
    trash[a][b]=1       #visited 처리
    res=1

    while q:
        x, y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny >=m:
                continue

            if trash[nx][ny]==0:  #if not visited
                trash[nx][ny]=1
                q.append([nx, ny])
                res+=1
    return res


n, m, k=map(int, input().split())
trash=[[0]*(m+1) for _ in range(n+1)]
answer=0
for _ in range(k):
    x, y=map(int, input().split())
    trash[x][y]=0       #탐색 전에 일단 모두 미방문 상태로 초기화
    
for i in range(1, n+1):
    for j in range(1, m+1):
        if trash[i][j] == 0:
            ans=bfs(trash, i, j)
            answer=max(ans, answer)
 
print(answer)

