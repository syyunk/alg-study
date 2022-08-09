n=int(input())
str=input()
p=[0]*n                     #QQ. 그냥 동적배열로 선언하는 것과의 차이?

for i in range(n):
    p[i]=int(input())       #피연산자값 받기

st=[]                       #str로 받은 문자열에 해당하는 피연산자값을 st에 넣기

#피연산자 리스트(스택)
for i in str:
    if 'A'<=i<='Z':
        st.append(p[ord(i)-ord('A')])       #a list에 b list값을 append로 고냥 바로 넣어버리기..
    else:
        str2=st.pop()
        str1=st.pop()

        if i=='+':
            st.append(str1+str2)
        elif i=='-':
            st.append(str1-str2)
        elif i=='*':
            st.append(str1*str2)     
        elif i=='/':
            st.append(str1/str2) 

#소수점 둘째자리까지 표기
#print(round(st[0], 2))  QQ. 왜 틀리징??        
print('%.2f' %st[0])