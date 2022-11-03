import sys
input=sys.stdin.readline
str=list(input().strip())
lst1=[]
tmp=1
answer=0

for i in range(len(str)):
    
    if str[i]=='(':
        lst1.append(str[i])
        tmp*=2

    elif str[i]=='[':
        lst1.append(str[i])
        tmp*=3

    elif str[i]==')':
        if not lst1 or lst1[-1]!='(':
            answer=0
            break
        if str[i-1]=='(':
            answer+=tmp

        tmp//=2     # answer에 tmp 값을 반영해줬으니 tmp임시값은 반영된 값에 해당하는 괄호의 값으로 나눠줌
        lst1.pop()

    elif str[i]==']':
        if not lst1 or lst1[-1]!='[':
            answer=0
            break
        if str[i-1]=='[':
            answer+=tmp
        tmp//=3
        lst1.pop()


if lst1:
    print(0)
else:
    print(answer)



