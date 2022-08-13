from collections import deque

n, m=map(int, input().split())
s = list(map(int, input().split())) # 궁금한 순서를 list에 저장
dq=deque([i for i in range(1, n+1)]) # 1부터 n까지 덱에 저장
cnt=0    # 2, 3번 연산 수행시 +1
for i in s:
   while True:
    if dq[0]==i:
        dq.popleft()
        break
    else:
        if dq.index(i)<len(dq)/2:
            while dq[0]!=i:
                dq.append(dq.popleft())
                cnt+=1
        else:
            while dq[0]!=i:
                dq.appendleft(dq.pop())
                cnt+=1

print(cnt)

