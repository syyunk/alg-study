t=int(input())

for _ in range(t):
    lst=list(map(int, input().split()))
    lst.sort()
    print(lst[-3])