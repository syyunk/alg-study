# 사탕게임

import sys
input=sys.stdin.readline

n=int(input())
candys=[list(input().strip()) for _ in range(n)]
cnt, answer=1, 1

#arr에서 인접한 것과 바꿨을 떄 가장 긴 연속한 부분을 리턴하는 함수 구현
def check(board):
    global cnt, answer
    for i in range(len(board)):
        cnt=1
        for j in range(1, len(board)):
            #열 기준 동일한 색상이라면
            if board[i][j]==board[i][j-1]:
                cnt+=1
            #이전과 다른 색상이라면 1로 초기화
            else:cnt=1

            #현재 cnt가 더 크면 answer 갱신
            if cnt>answer: answer=cnt
        
        cnt=1
        for j in range(1, len(board)):
            #행 기준 동일색상이라면
            if board[j][i]==board[j-1][i]:
                cnt+=1
            #이전과 다른 색상이라면 1로 초기화
            else:cnt=1

            #현재 cnt가 더 크면 answer 갱신
            if cnt>answer: answer=cnt
    return answer    


for i in range(n):
    for j in range(n):
        #i=x축, j=y축
        #열 바꾸기 - n*n 범위 내에서
        if j+1<n:
            #인접한 열과 바꾸기
            candys[i][j], candys[i][j+1]=candys[i][j+1], candys[i][j]
            answer=max(check(candys), answer)
            #바꿨던 것을 원래대로 돌려놓기
            candys[i][j], candys[i][j+1]=candys[i][j+1], candys[i][j]

        #행 바꾸기
        if i+1<n:
            #인접한 행과 바꾸기
            candys[i][j], candys[i+1][j]=candys[i+1][j], candys[i][j]
            answer=max(check(candys), answer)
            #바꿨던 것을 원래대로 돌려놓기
            candys[i][j], candys[i+1][j]=candys[i+1][j], candys[i][j]

print(answer)
