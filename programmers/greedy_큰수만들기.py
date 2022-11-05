from itertools import combinations


def solution(number, k):
    for comb in combinations(number, k):
        comb=list(comb)
        comb.sort(reverse=True)
        print(comb)
    return comb[0]

print(solution("1924", 2))