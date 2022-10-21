from collections import deque


n, k = map(int, input().split())
max=100000
d=[0]*(max+1)

def bfs():
    q=deque()
    q.append(n)
    while q:
        now=q.popleft()
        if now==k:
            print(d[now])
            break

        for j in (now-1, now+1, now*2):
            if 0<=j<=max and not d[j]:      # d[j]=0 => -1, +1, *2 중 간 적 없는 지점이면
                d[j]=d[now]+1
                q.append(j)

bfs()
            

