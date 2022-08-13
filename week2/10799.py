str=list(input())
answer=0
st=[]

for i in range(len(str)):
    if str[i]=='(':
        st.append(str[i])
    else:
        if str[i-1]==')':
            st.pop()
            answer+=1
        else: 
            st.pop()
            answer+=len(st)

print(answer)