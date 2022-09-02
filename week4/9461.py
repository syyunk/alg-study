p=[0 for i in range(101)]
p[1]=1
p[2]=1
p[3]=1
for i in range(4, 101):
    p[i]=p[i-3]+p[i-2]

n=int(input())
for i in range(n):
    k=int(input())
    print(p[k])
