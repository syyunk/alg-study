import sys
sys.setrecursionlimit(100000)

n=int(input())
matrix=[list(input().rstrip()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

#정상(no_cnt), 색약(yes_cnt)인 각 경우의 카운트 초기화
no_cnt, yes_cnt=0, 0
dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

def dfs(x, y):
    visited[x][y]=True
    #현재 위치의 색 저장
    cur_color=matrix[x][y]
    
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        #범위를 벗어났다면
        if nx<0 or ny<0 or nx>=n or ny >= n:
            continue
        #탐색한 곳이 아직 방문처리되지 않은 곳이고
        if visited[nx][ny]==False:
            # 탐색 전 위치의 색과 탐색한 곳의 색이 같다면 방문처리
            if matrix[nx][ny] == cur_color:
                dfs(nx, ny)

# 정상인일 때의 카운트
for i in range(n):
    for j in range(n):
        #미방문한 곳이면 dfs탐색
        if visited[i][j]==False:
            dfs(i, j)
            no_cnt+=1

# 색약인일 때의 카운트
for i in range(n):
    for j in range(n):
        if matrix[i][j]=='G':
            matrix[i][j]='R'
        #등호 갯수 주의!!(=대입, ==비교) 
        #or matrix[i][j].replace('G', 'R')
            
#matrix 재사용할 것이기 때문에 방문 리스트 재선언
visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        #미방문한 곳이면 dfs탐색
        if visited[i][j]==False:
            dfs(i, j)
            yes_cnt+=1

print(no_cnt, yes_cnt)