
def fibo(k):
    if k<=1:
        return k
    return fibo(k-1)+fibo(k-2)

n=int(input())
print(fibo(n))