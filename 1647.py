import sys
from collections import deque

input = sys.stdin.readline


n, m = map(int, input().split())
edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
edges.sort(key = lambda x :x[2])

parent = [i for i in range(n+1)]
#union-find 초기화
def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x]) 
    return parent[x]

def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b: # 작은 쪽이 부모가 된다. (한 집합 관계라서 부모가 따로 있는 건 아님)
        parent[b] = a
    else:
        parent[a] = b        

def same_parent(a, b):
    return get_parent(a) == get_parent(b)



res = 0
max_cost = 0
for a, b, cost in edges:
    if not same_parent(a, b):
        union_parent(a, b)
        res += cost
        max_cost = max(max_cost, cost)
print(res - max_cost)