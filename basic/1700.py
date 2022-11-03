#실패..
import sys
input=sys.stdin.readline

n, k = map(int, input().split())
nums=list(map(int, input().split()))
adaptor=[0]*n
cnt=0
tmp, tmp_i=0, 0

for i in range(k):
    # 어댑터에 이미 꽂혀있다면
    if i in adaptor: continue

    # 어댑터에 공란이 있다면
    elif 0 in adaptor:  
        #list.index(x) = list에서 x가 처음 등장하는 인덱스를 리턴
        adaptor[adaptor.index(0)]=i     
    else:
        for j in adaptor:
            # 현재 꽂혀있는 애가 추후 사용되지 않는다면
            if j not in nums[i:]:
                # 그 자리를 현재 사용할 애의 플러그로 업데이트
                tmp=j
                break
            #추후 사용할 플러그이고, 가장 마지막에 사용할 플러그보다 멀면
            #=꽂혀있는 애들 중 더 나중에 사용되는 것을 뽑기 위해
            elif nums[i:].index(j)>tmp_i:
                tmp_i=nums[i:].index(j)
                tmp=j
        # 가장 마지막에 사용할 플러그의 인덱스를 구해 현재 사용할 플러그로 업데이트
        adaptor[adaptor.index(tmp)]=i
        #다음 루프에서 사용해야 하니 초기화
        tmp=tmp_i=0
        cnt+=1
    
print(cnt)
                
            