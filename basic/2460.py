sum, maxsum=0, 0


for _ in range(10):
    m, n=map(int, input().split())
    if maxsum<sum:
        maxsum=sum
    sum=sum-m+n

print(maxsum)