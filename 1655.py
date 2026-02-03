import sys
import heapq

input = sys.stdin.readline
n = int(input())
left = []   # 최대
right = []  # 최소

for _ in range(n):
    x = int(input())
    if not left or x <= -left[0]:
        heapq.heappush(left, -x)
    else:
        heapq.heappush(right, x)

    # 균형 맞추기: left가 항상 크거나 같고 크기 차이는 최대 1
    if len(left) < len(right):
        heapq.heappush(left, -heapq.heappop(right))
    elif len(left) - len(right) > 1:
        heapq.heappush(right, -heapq.heappop(left))

    print(-left[0])
 #중간값 == 작은 힙의 루트(가장큰값 == -left[0])