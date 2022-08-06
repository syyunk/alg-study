n=int(input())


for i in range(n):
    s=[]
    str=input()

    for j in range(str):                # for j in str로 수정하면 에러 안남
        if j=="(" :
            s.append(j)

        elif j==")":
            if s:
                s.pop()
            else:
                print("NO")
                break
    else:
        if not s :
            print("YES")
        else : print("NO")
    
