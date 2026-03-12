import sys
input = sys.stdin.readline

n = int(input())
ls= []
for _ in range(n):
    ls.append(input().strip())

weight = {}

for word in ls:
    length = len(word)
    for i, ch in enumerate(word):
        weight[ch] = weight.get(ch, 0) + 10 ** (length - i -1)

weight = sorted(weight.items(), key=lambda x: x[1], reverse=True) #가중치 정렬 

num = 9
mapping = {}
for ch , w in weight:
    mapping[ch] = num
    num -=1

res = 0

for word in ls:
    num = 0
    for ch in word:
        num = num*10 + mapping[ch] #각 단어의 숫자값 계산
    res += num
print(res)