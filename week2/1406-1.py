import sys

st1=list(sys.stdin.readline().rstrip())
st2=[]

for i in range(int(input())):
    cmd=list(sys.stdin.readline().split())
    if cmd[0]=='L':
        if st1:
            st2.append(st1.pop())

    elif cmd[0]=='D':
        if st2:
            st1.append(st2.pop())
    elif cmd[0]=='B':
        if st1:
            st1.pop()
    else:
        st1.append(cmd[1])

st1.extend(reversed(st2))   
#st2를 뒤집어 extend하는 과정에서 st2.reverse할 경우 st2이 빈 배열이면 에러남
print(''.join(st1))