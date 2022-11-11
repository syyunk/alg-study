from itertools import combinations

answer=[]
def solution(number, k):
    answer=combinations(list(number), len(number)-k)
    return ''.join(sorted(answer, reverse=True)[0])

print(solution("1924", 2))