# 10451과 유사

n=int(input())
k=int(input())

visited=[False]*(n+1)
gr=[[] for _ in range(n+1)]
res=0

for _ in range(k):
    a, b=map(int, input().split())
    gr[a].append(b)
    gr[b].append(a)

def dfs(start):
    global res
    visited[start]=True
    for i in gr[start]:
        if not visited[i]:
            dfs(i)
            visited[i]=True
            res+=1

dfs(1)
print(res)




    
