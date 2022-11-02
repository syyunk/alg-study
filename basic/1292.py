a, b=map(int, input().split())
lst=[0]

for i in range(b+1):
    for j in range(i):
        lst.append(i)

print(lst)
print(sum(lst[a:b+1]))