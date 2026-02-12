import sys

input = sys.stdin.readline

n, s = map(int, input().split())
a = list(map(int, input().split()))

start, end = 0, 1
cur_sum = a[0]
min_length = float('inf')

while start < n and end <= n:
    if cur_sum >= s:
        min_length = min(min_length, end - start)
        cur_sum -= a[start]
        start +=1
    else:
        if end == n:
            break
        cur_sum += a[end]
        end +=1

if min_length == float('inf'):
    print(0)
else:
    print(min_length)