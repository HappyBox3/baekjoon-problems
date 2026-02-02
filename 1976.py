import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

parent = list(range(n+1))

def find(x): #경로 압축
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[rb] = ra

# 인접행렬 전부 읽고 union
for i in range(n):
    row = list(map(int, input().split()))
    for j, val in enumerate(row):
        if val:
            union(i+1, j+1)

plan = list(map(int, input().split()))

root = find(plan[0])
print("YES" if all(find(p) == root for p in plan) else "NO")