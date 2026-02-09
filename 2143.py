import sys
from collections import Counter
input = sys.stdin.readline

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

res = 0
c = Counter()

for s in range(n):
    for e in range(s, n):
        c[sum(A[s:e+1])] += 1


for s in range(m):
    for e in range(s, m):
        t =  T - sum(B[s:e+1])
        res += c[t]
print(res)