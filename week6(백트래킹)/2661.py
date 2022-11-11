import sys
sys.setrecursionlimit(10**4)

n=int(input())


# n자리수인 수열 중 좋은 수열 찾기 
def isPromise(num):
    length=len(num)
    for i in range(1, length//2+1):
        if num[-i:] == num[-(i*2):-i]:
            return False
    else:               #왜???
        return True

def recur(num):
    global n
    #종료조건
    if len(num)==n:
        print(num)
        exit()      # return으로 종료하면 recur는 길이가 n인 좋은 수열을 계속해서 찾음
    for i in '123':
        if isPromise(num + str(i)):
            recur(num+str(i))
    return

recur('1')