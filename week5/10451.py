import sys


def dfs(start):     # 정의 다시
    visited[start]=True
    for i in arr[start]:
        if not visited[i]:
            dfs(i)    
            visited[i]=True


for _ in range(int(input())):
    res=0
    n=int(sys.stdin.readline())
    arr=[0]+list(map(int, sys.stdin.readline().split()))
    visited=[False]*(n+1)

    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
            visited[i]=True
            res+=1
    print(res)


