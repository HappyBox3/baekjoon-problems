import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = list(map(int, input().split()))
p = data[0]
truth = set(data[1:]) if p > 0 else set()

parties = []
for _ in range(m):
    dt = list(map(int, input().split()))
    cnt = dt[0]
    people = dt[1:1+cnt]
    parties.append(people)

# 반복 전파
changed = True
while changed:
    changed = False
    for people in parties:
        if any(person in truth for person in people):
            before = len(truth)
            truth.update(people) #중복 자동제거
            if len(truth) != before:
                changed = True

# 진실을 모르는 파티 수
res = sum(1 for people in parties if not any(person in truth for person in people))
print(res)
