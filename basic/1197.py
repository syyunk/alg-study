import sys
input=sys.stdin.readline

#최소 스패닝 트리
#kruskal알고리즘 = 최소신장거리 찾기

def findParent(parent, x):
    #부모노드 찾을 때까지 재귀호출
    if parent[x]!=x:
        parent[x]=findParent(parent, parent[x])
    return parent[x]

#두 원소가 속한 집합 합치기 = 부모 노드 통일시키기
def unionParent(parent, a, b):
    a=findParent(parent, a)
    b=findParent(parent, b)

    if a<b:
        #b=3, a=2 , 3->2, 2->1인 경우 3->1
        parent[b]=a
    else:
        parent[a]=b

#vertax 개수와 간선(union 연산)의 개수 입력받기
node, edge=map(int, input().split())
parent=[0]*(node+1)
#부모 테이블에서 부모를 자기 자신으로 초기화
for i in range(1, node+1):
    parent[i]=i

#모든 간선에 대한 정보 입력받기
edges=[]
res=0
for _ in range(edge):
    a, b, cost=map(int, input().split())
    #비용순 정렬 위해 튜플의 첫쨰 원소를 cost로 저장
    edges.append((cost, a, b))
    
#간선을 비용순으로 정렬
edges.sort()

#간선을 하나씩 확인
for edge in edges:
    cost, a, b=edge
    #사이클이 발생하지 않는 경우만 집합에 포함시킴
    if findParent(parent, a)!=findParent(parent, b):
        unionParent(parent, a, b)
        res+=cost

print(res)
