n=int(input())
a=list[10007]

a[1]=1
a[2]=2
a[3]=3
a[4]=4
for i in range(5, 10007):
    a[i]=a[i-1]+a[i-2]        

print(a[n])
