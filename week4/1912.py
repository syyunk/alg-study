n=int(input())
a=list(map(int, input().split()))
dp=[0 for i in range(n)]

def sol(n):
    for i in range(n):
        dp[i]+=a[i]
        
        if(dp[i] < dp[i-1]):
            break
    return dp[i-1]

print(sol[n])
