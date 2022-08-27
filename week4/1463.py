n= int(input())
temp=[0]*(n+1)
cnt=0

    

def makeOne(n):
    for i in range(n):
        if n%3==0:
            m=n/3
            cnt+=1
            temp[i]=m
        if n%2==0:
            m=n/2
            cnt+=1
            temp[i]=m
        else: 
            m=n-1
            temp[i]=m
        if n==1: return cnt

for i in range(n):
    



print(cnt)


