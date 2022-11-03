import sys
input=sys.stdin.readline

n=int(input())
nums=list(map(int, input().split()))
lst=list(map(int, input().split())) # + - * //
max, min=-1e9, 1e9                  # 1e9 = 1*10 **9
answer=nums[0]                      # 입력받은 수 중 첫 번째 숫자  

def dfs(idx):
    global max, min, answer
    if idx==n:
        if answer>max:
            max=answer
        if answer<min:
            min=answer

    for i in range(4):
        # tmp에 answer를 담지 않으면 출력 초과가 나는 이유?
        # 함수(모듈)에서 전역 변수를 할당할 일이 생기면 그 할당시점에 컴파일러가 로컬변수로 간주 -> 오류 발생
        tmp=answer
        if lst[i]>0:
            if i==0:
                answer+=nums[idx]
            elif i==1:
                answer-=nums[idx]
            elif i==2:
                answer*=nums[idx]
            else:
                if answer>=0:
                    answer//=nums[idx]
                else:
                    answer = abs(answer)//nums[idx] *-1
            lst[i]-=1
            dfs(idx+1)
            answer=tmp
            #원래 상태로 돌려 모든 경우의 수 찾기(백트래킹)
            lst[i]+=1

dfs(1)
print(max)
print(min)