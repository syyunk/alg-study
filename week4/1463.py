n= int(input())
temp=[0]*(1000001)


for i in range(2, n+1):
    # 7을 1로 연산횟수는 [7-1을 1로 만드는 연산횟수]+1(3. 1을 뺀다) 
    temp[i]=temp[i-1]+1
        
    # temp[6] = n/2 한 번+ n/2의 결과인 3을 1로 만드는 temp[3] = 1+temp[6//2]
    # 6을 3으로 나눌 경우는 temp[6]=1+temp[6//3]    => 두 값을 비교해 더 작은 값이 temp[6]
    if i%3==0:
        temp[i]=min(temp[i], temp[i//3]+1)
    if i%2==0:
        temp[i]=min(temp[i], temp[i//2]+1)

print(temp[ㅜ])
