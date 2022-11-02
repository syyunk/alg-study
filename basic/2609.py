n, m = map(int, input().split())

def g(n, m):
    while m>0:
        n, m=m, n%m
    return n

def l(n,m):
    return n*m // g(n, m)

print(g(n, m))
print(l(n, m))