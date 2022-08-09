
n=int(input())

for i in range (n):
    cnt=0
    paper,widx=map(int, input().split())           #que[wonderidx]의 순서 구하기
    s=list(map(int, input().split()))               #paper의 수 만큼 주어지는 중요도(차례대로)
    b=[0 for i in range(paper)]                     #문서 수만큼 0으로 초기화된 배열 선언
    b[widx]=1                                       #타겟 요소를 1로 설정
    #중요도 리스트(s)의 첫 번째 인덱스 값이 최댓값이 될 때까지 나머지 값들을 뒤로 보내주기
    while True:                        # QQ. While 1은 왜 에러?
        if s[0]==max(s):                            #젤 높은 중요도라면 cnt+1
            cnt+=1
            
            if b[0]!=1:                             #타겟이 아니라면
                del s[0]
                del b[0]
            else:
                print(cnt)
                break
        else:
            s.append(s.pop(0))                      #중요도 순서대로 처리해주기 위해 max값이 아니라면 맨뒤로 보냄
            b.append(b.pop(0))

                