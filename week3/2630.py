import sys

n=int(input())
paper=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]



result=[]

def cut(x, y, n):
    chk=True
    color=paper[x][y]

    for i in range(x, x+n):
        if not chk:break

        for j in range(y, y+n):
            if color!=paper[i][j]:
                chk=False
                cut(x, y, n//2)     # 1사분면
                cut(x, y+n//2, n//2)    #2사분면
                cut(x+n//2, y, n//2)    # 3사분면
                cut(x+n//2, y+n//2, n//2)   #4사분면
                break
    if chk:
        if color:result.append(1)       #파란종이
        else: result.append(0)            #흰종이

cut(0, 0, n)
print(result.count(0))
print(result.count(1))