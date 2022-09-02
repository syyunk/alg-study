n=int(input())
a=list(map(int, input().split()))
dp=[0 for i in range(n)]

for i in range(n):
    for j in range(i):
        # 자기자신보다 작은 숫자들로 만들 수 있는 가장 큰 길이를 구하고 +1(자기자신) 
        if a[i]>a[j] and dp[i]<dp[j]:
            dp[i]=dp[j]
    dp[i]+=1
print(max(dp))

    