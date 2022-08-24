
from collections import deque


n = int(input())
data=list(map(int, input().split(" ")))
res=["0"]*n

st=deque()
for i in range(n-1, -1, -1):
    # 스택에 값이 남아있고 가장 최근에 저장된 data가 data[i]보다 작은 경우 => data[i] 탑이 수신함
    while len(st) !=0 and st[-1][0] < data[i]:     
        # 스택의 가장 최근에 저장된 data의 idx번째 res(=idx번째 탑의 발신을 수신하는 탑의 번호)= data[i]탑의 번호    
        res[st[-1][1]] = str(i+1)
        st.pop()

    st.append((data[i], i))

print(" ".join(res))