#백트래킹-스도쿠
# 1. 전체를 돌면서 0의 위치와 개수 파악
# 2. 9*9의 범위를 n번쨰행 n번째열 쌍으로 나눠서 생각
# 3. 1에서 파악한 0의 위치가 2의 범위에 포함되고, 2의 범위 안 숫자들이 아닌 숫자를 해당 범위의 0위치에 넣음

import sys
input=sys.stdin.readline

sdk=[list(map(int, input().rstrip().split())) for _ in range(9)]
spot=[]

for i in range(9):
    for j in range(9):
        if sdk[i][j]==0:
            spot.append((i, j))

#행 check
def checkRow(x, a):
    for i in range(9):
        if a==sdk[x][i]:
            return False
    return True

def checkCol(y, a):
    for i in range(9):
        if a==sdk[i][y]:
            return False
    return True

def checkRect(x, y, a):
    nx=x//3 * 3
    ny=y//3 * 3
    for i in range(3):
        for j in range(3):
            if a==sdk[nx+i][ny+j]:
                return False
    return True

def dfs(idx):
    #종료조건
    if idx ==len(spot):
        for i in range(9):
            print(*sdk[i])
        exit(0)

    # 빈칸(0) 말고 1~9인 애들만 탐색
    for i in range(1, 10):      
        x=spot[idx][0]
        y=spot[idx][1]
    
        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            sdk[x][y]=i
            dfs(idx+1)
            sdk[x][y]=0

dfs(0)