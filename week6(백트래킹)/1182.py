import sys
input=sys.stdin.readline

n, s=map(int, input().split())
nums=list(map(int, input().split()))    #[-7, -3, -2, 5, 8]
#nums=list(int, input().split())        #['-7', '-3', '-2', '5', '8']
print(nums)
cnt=0

def backtr(idx, res):
    global cnt
    if idx>=n:
        return
    
    #수열에 현재 idx 정수를 더하기
    res+=nums[idx]

    #현재 수열의 원소 합이 s라면 cnt+=1
    if res == s:
        cnt+=1
    
    backtr(idx+1, res)              #현재 nums[idx]를 선택한 경우의 가지
    backtr(idx+1, res-nums[idx])   # 현재 nums[idx]를 선택하지 않은 경우의 가지

#backtr(0, 0)
#print(cnt)

