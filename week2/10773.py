n=int(input())
st=[]

for i in range(n):
    str=int(input())
    if str==0:
        st.pop()
    else:
        st.append(str)
print(sum(st))