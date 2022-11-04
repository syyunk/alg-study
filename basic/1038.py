#감소하는 수
#조합 말고 재귀로 푸는 방법도 공부..

import sys
from itertools import combinations

input=sys.stdin.readline

n=int(input())
answer=[]

#최대 감소하는 수는 9876543210
for i in range(1, 11):                               #1자리부터 10자리까지 
    for comb in combinations(range(0, 10), i):      #0~9로 조합되는 중복x인 수 중에서
        comb=list(comb)
        comb.sort(reverse=True)                     #해당 조합을 감소하는 수로 변경

        answer.append(int("".join(map(str, comb))))
answer.sort()

try:
    print(answer[n])
except:
    print(-1)