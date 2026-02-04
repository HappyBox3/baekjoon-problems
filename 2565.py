import sys

input = sys.stdin.readline

n = int(input())
ls = []
for _ in range(n):
    a, b = map(int, input().split())
    ls.append((a, b))

ls.sort()
B = [b for _, b in ls]

dp = [1]*n

for i in range(n):
    for j in range(i):
        if B[j] < B[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))

#:LIS 앞 순서의 모든 원소에서 끝나는 최장 증가 수열들의 길이 중 가장 긴 것을 골라
# 1을 더한 것이 곧 현재 수에서 끝나는 최장 증가 수열의 길이