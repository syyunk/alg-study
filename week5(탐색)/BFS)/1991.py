
n=int(input())
gr=[[] for _ in range(n+1)]

start=64

for _ in range(n):
    a, b, c=map(int, input().split())
    gr[a].append[b, c]
    gr[b].append[a, c]
    gr[c].append[a, b]

