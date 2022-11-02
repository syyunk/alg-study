n=int(input())
nums=list(map(int, input().split()))
add, sub, mul, div=map(int, input().split()) # + - * //
max, min=1e9, -1e9      # 1e9 = 1*10 **9
answer=nums[0]      # 입력받은 수 중 첫 번째 숫자  

def dfs(i):
    global add, sub, mul, div, max, min
    for i in range(4):
        tmp=answer
        if i==0:
            answer+=nums[i]
        elif i==1:
            answer-=nums[i]
        elif i==2:
            answer*=nums[i]
        else:
            if answer>=0:
                answer //= nums[i]
            else:
                answer = (-answer // nums[i])*-1
        
        dfs(i+1)
        answer=tmp
        

