import sys
input=sys.stdin.readline

n=int(input())
var=[list(map(str, input().strip())) for _ in range(n)]
print(max(len(var[i]) for i in range(n)))


for i in range(n):
    for j in range(n):
        if max(len(var[i]))<len(var[j]):
            for k in range(len(var[j])):
                #앞에서 이미 숫자로 바뀐 알파벳이라면
                if var[j][k]<=9:
                    continue
                #str을 int로 
                int(var[j])
                var[j][k]=9-k
            
            

            

