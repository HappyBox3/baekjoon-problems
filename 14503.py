import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[False] * m for _ in range(n)]
cnt = 0

while True:
    # 1. 현재 칸 청소
    if not visited[r][c]:
        visited[r][c] = True
        cnt += 1

    moved = False

    # 2. 왼쪽부터 4방향 확인
    for _ in range(4):
        d = (d + 3) % 4  # 왼쪽 회전
        nx = r + dx[d]
        ny = c + dy[d]

        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and board[nx][ny] == 0:
                r, c = nx, ny
                moved = True
                break

    # 이동했으면 다시 1번부터
    if moved:
        continue

    # 3. 네 방향 모두 못 가면 뒤로 이동
    back_dir = (d + 2) % 4
    bx = r + dx[back_dir]
    by = c + dy[back_dir]

    # 뒤가 벽이면 종료
    if board[bx][by] == 1:
        break
    else:
        r, c = bx, by

print(cnt)
