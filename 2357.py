import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = [0] + [int(input()) for _ in range(n)]
tree = [(0,0)] * (4*n)


def build(node, start, end):
    if start == end:
        tree[node] = (arr[start], arr[start])
    else:
        mid = (start + end) // 2
        build(node*2, start, mid)
        build(node*2+1, mid+1, end)

        left = tree[node*2]
        right = tree[node*2+1]

        tree[node] = (
            min(left[0], right[0]),
            max(left[1], right[1])
        )

def query(node, start, end, left, right):
    #완전 미포함
    if right < start or end < left:
        return (float('inf'), -float('inf'))

    #완전 포함
    if left <= start and end <= right:
        return tree[node]
    
    #일부 포함
    mid = (start+end)//2
    l_val = query(node*2, start, mid, left, right)
    r_val = query(node*2+1, mid+1, end, left, right)

    return (
        min(l_val[0], r_val[0]),
        max(l_val[1], r_val[1])
    )

build(1, 1, n)

for _ in range(m):
    a, b = map(int, input().split())
    res = query(1, 1, n, a, b)
    print(res[0], res[1])


