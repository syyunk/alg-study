n=int(input())


for i in range(n):
    s=[]
    str=input()

    for j in str:                # for j in range(len(str)) -> 0, 1, 2, 3...
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
    
