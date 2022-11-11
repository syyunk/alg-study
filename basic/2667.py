#단지번호 붙이기
#bfs
from collections import deque
import sys

input=sys.stdin.readline

n=int(input())
gr=[list(map(int, input().rstrip())) for _ in range(n)]
cnt=0
res=[]                      #각 단지당 집의 수를 담을 리스트 선언

dx=[0, 0, 1, -1]
dy=[1, -1, 0, 0]

def bfs(gr, a, b):
    global cnt
    q=deque()
    q.append([a, b])        #a, b를 큐에서 그대로 뺴기 위해 append
    gr[a][b]=0              #첫번째 집 (a, b)를 방문 처리
    cnt=1                   #첫번째집 방문처리 했으므로 cnt+1
    
    while q:
        x, y=q.popleft()
        gr[x][y]=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny >=n:
                continue
            #미방문한 집이라면
            if gr[nx][ny] == 1:
                gr[nx][ny]=0            #방문처리
                q.append([nx, ny])      #탐색한 곳의 좌표를 큐에 추가
                cnt+=1
    return cnt

for i in range(n):
    for j in range(n):
        if gr[i][j]==1:
            cnt=bfs(gr, i, j)
            res.append(cnt)

res.sort()

print(len(res))
for i in res:
    print(i)