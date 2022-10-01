 n=int(input())
 list=list(map(int, input().split()))

 dp=[n in range(list)]

 for i in range(n):
    for j in range(i):
        #현재 인덱스값과 이전 인덱스를 비교해 현재 수가 이전 수보다 크다면
        if list[i]>list[j]:
    #현재 인덱스 위치에 가장 큰 부분 수열의 합 vs 이전 인덱스 위치에 가장 큰 부분수열의 합+현재 수 비교해 dp를 채우기
            dp[i]=max(dp[i], dp[j]+list[i])
print(max(dp))
