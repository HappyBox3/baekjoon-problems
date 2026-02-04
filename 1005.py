import sys
from collections import deque

input = sys.stdin.readline

t = int(input())  # 테스트 케이스 수

for _ in range(t):
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split())) #(1-indexed) 
    graph = [[] for _ in range(n + 1)]
    indegree = [0]*(n + 1) #진입차수

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] +=1 

    w = int(input())

    dp = [0]*(n+1)
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            dp[i] = time[i]
            q.append(i)
    
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            dp[nxt] = max(dp[nxt], dp[cur] + time[nxt]) # 최대 시간 갱신(가장 느린 선행건물)
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

    print(dp[w])