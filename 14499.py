import sys

input = sys.stdin.readline

n, m, x, y , k = map(int, input().split())

jido = [list(map(int, input().split())) for _ in range(n)] #지도
com = list(map(int, input().split())) 

dx = [0, 0, 0, -1, 1] # 
dy = [0, 1, -1, 0, 0] # 

dice = [0] * 6

for cmd in com:
    nx = x + dx[cmd]
    ny = y + dy[cmd]
   
    if not (0 <= nx < n and 0 <= ny < m):
        continue

    x, y = nx, ny
    
    top, bottom, north, south, west, east = dice #인덱스 포지션 
    if cmd == 1:  # 동
        dice = [west, east, north, south, bottom, top]
    elif cmd == 2:  # 서
        dice = [east, west, north, south, top, bottom]
    elif cmd == 3:  # 북
        dice = [south, north, top, bottom, west, east]
    elif cmd == 4:  # 남
        dice = [north, south, bottom, top, west, east]

    if jido[x][y] == 0:
        jido[x][y] = dice[1]
    else:
        dice[1] = jido[x][y]
        jido[x][y] = 0
    
    print(dice[0])