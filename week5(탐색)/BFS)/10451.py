import sys
sys.setrecursionlimit(10000)


def dfs(start):     
    i=arr[start]
    if not visited[i]:
        visited[i]=True
        dfs(i)

for _ in range(int(sys.stdin.readline())):  # 반복할 횟수
    res=0
    n=int(sys.stdin.readline())             # 만들 순열 자릿수
    arr=[0]+list(map(int, sys.stdin.readline().split()))
    visited=[False]*(n+1)

    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
            res+=1
    print(res)


