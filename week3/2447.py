n=int(input())

def star(len):
    stars=[]
    if len==3:
        return ['***', '* *', '***']
    
    for i in range(3*len(n)):
        # n( =len(basic) ) / 3의 나머지가 1인 경우(1, 4, 7) 공백으로 두기(n의 길이만큼)
        if i//len(n)==1:
            stars.append(n[ i%len(n) ]) + " "*len(n) + n[i%len(n)]
        # n이 3의 배수라면 공백 없이 별을 모두 채움
        else:
            stars.append(n[i%len(n)]*3)
    return stars

basic=["***", "* *", "***"]
k=0


while n != 3:
    n = int(n/3)
    k+=1        # 재귀함수를 몇 번 실행할지 정하는 변수

for i in range(k):
    basic = star(basic)
for i in basic:
    print(i)

