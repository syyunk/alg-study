n=int(input())
cnt=0
row=[0]*n


# row[x]=i = 좌표 (x, i)
def isNeighbor(x):
    for i in range(x):
        # 퀸을 놓을 위치가 이전에 퀸을 놓은 위치의 좌표와 열이 같거나 같은 대각선상에 있으면 false
        if row[x]==row[i] or abs(row[x]-row[i])==abs(x-i):  
            return False
    return True

#isNeighbor가 True이면 방문처리
#=모든 경우의 수 중 가능한 경우만 매 탐색마다 판별해 dfs탐색
def nqueen(x):
    global cnt
    if x==n:
        cnt+=1
        return
    else:     
        for i in range(n):
            row[x]=i
            if isNeighbor(x):
                nqueen(x+1)

nqueen(0)
print(cnt)