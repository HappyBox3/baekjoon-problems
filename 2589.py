from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(sx, sy):
    visited = [[-1]*m for _ in range(n)]  
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = 0
    max_dist = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 'L' and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1 # 현재 위치에서 다음 위치까지의 거리를 계산하여 저장
                    max_dist = max(max_dist, visited[nx][ny])
                    q.append((nx, ny))

    return max_dist

answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            answer = max(answer, bfs(i, j))

print(answer)