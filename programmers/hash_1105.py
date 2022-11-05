from collections import Counter

def solution(participant, completion):
    answer=''
    mix=participant+completion
    answer = Counter(mix)
    for i in range(len(answer)):
        if answer.values(i)==0:
            ans=answer.keys(i)

    return ans