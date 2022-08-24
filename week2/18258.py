from sys import stdin

input()

# 덱 없이 큐 구현하기
# 시간복잡도 문제 피하려면 큐의 출구 인덱스를 따로 저장!
s, com=[], stdin.readlines()
cnt=0

for i in com:
    c=i.split()
    if c[0] == "push":
        s.append(c[1])
    elif c[0] == "pop":
        if len(s)>cnt:
            print(s[cnt])
            cnt+=1
        else: print(-1)
    elif c[0] == "size":
        print(len(s)-cnt)
    elif c[0] == "empty":
        if len(s)==cnt:
            print(1)
            cnt=0
            s=[]
        else : print(0)
    elif c[0] == "front":
        if len(s)>cnt: print(s[cnt])
        else: print(-1)
    elif c[0] =="back" :
        if len(s)>cnt: print(s[-1])
        else : print(-1)
