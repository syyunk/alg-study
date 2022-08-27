n=int(input())
paper=[]

def cut():
    for x in range(n):
        for y in range(n):
            if paper[x][y]==0:
                return len(paper)
            if paper[x][y]==1:
                return len(paper)
            