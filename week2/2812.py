n, k = map(int, input().split())
num=list(input())

# 숫자 제거 횟수 초기화
exK=k

res=[]

#앞에서부터 차례대로 가면서 큰 수만 남기면 됨
for i in range(n):
    while exK and res:
        # 스택 리스트의 최근 숫자가 num[i]보다 작으면 pop하고 숫자 제거 횟수-1
        if res[-1]<num[i]:      
            res.pop()
            exK-=1
        else:
            break
    res.append(num[i])

# print(''.join(res[:n-k])) QQQ. 설명