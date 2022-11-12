
def dfs(len, idx):
    if len==l:
        mo=0
        ja=0
        for i in range(l):
            if answer[i] in 'aeiou':mo+=1 
            else:ja+=1

        if mo>=1 and ja>=2:
            print(''.join(answer))
        return

    for i in range(idx, c):
        if visited[i]==0:
            answer.append(var[i])
            visited[i]=1
            dfs(len+1, i+1)
            visited[i]=0
            answer.pop()


l, c = map(int, input().split())
var=sorted(list(map(str, input().split())))
answer=[]
visited=[0 for _ in range(c)]
dfs(0, 0)