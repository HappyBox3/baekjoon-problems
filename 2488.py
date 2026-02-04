import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
n = int(input())

def starlink(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']

    star = starlink(n // 2)
    res =[]

    for i in star:
        res.append(' '*(n//2)+i+' '*(n//2))
    for i in star:
        res.append(i+' '+i)
    return res

print('\n'.join(starlink(n)))