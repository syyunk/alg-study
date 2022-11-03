s=int(input())
cnt=1

while cnt*(cnt+1)/2<=s:
    cnt+=1

print(cnt-1)


