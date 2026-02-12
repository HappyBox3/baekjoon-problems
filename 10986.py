import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

prefix = 0
count = [0] * m
count[0] = 1   # prefix가 처음부터 m으로 나눠떨어지는 경우

answer = 0

for num in a:
    prefix = (prefix + num) % m
    answer += count[prefix]
    count[prefix] += 1

print(answer)
