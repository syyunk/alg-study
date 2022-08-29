a=int(input()) 

# n=0, 1, 2일 때의 각 0호출회수와 1 호출회수 초기화
# 이미 구한 숫자를 또 다시 구하는 일이 없게 <- DP
zero=[1, 0, 1]
one = [0, 1, 1]

def cnt(n):
    if len(zero) <= n:      # >면 이미 zero와 one 배열에 저장되어있는 값을 출력하면 됨
        for i in range(len(zero), n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print("%d %d"%(zero[n],one[n]))

for i in range(a):
    n=int(input())
    cnt(n)