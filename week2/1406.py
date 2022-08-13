import sys


txt=list(input())
n=int(input())
cr=len(st)

for i in range(n):      #반복문으로 입력 받을 땐 시간복잡도 고려해 input() 대신 sys.stdin.readline
    cmd=list(sys.stdin.readline().split())
    
    if cmd[0] == "L" and cr >0:
        cr -=1
    elif cmd[0]=="D" and cr <len(txt):
        cr+=1
    elif cmd[0] =="B" and cr>0:
        txt.pop(cr-1)
        cr -=1
    elif cmd[0] =="P":
        txt.insert(cr, cmd[1])
        cr +=1

for i in range(len(txt)):
    print(txt[i], end="")
