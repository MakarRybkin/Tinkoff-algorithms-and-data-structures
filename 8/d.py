
from sys import stdin

A = []
ST = []


def build(node, L, R):
    global A, ST
    if (L == R):
        ST[node] = A[L]

    else:

        mid = (L + R) // 2
        build(2 * node, L, mid)
        build(2 * node + 1, mid + 1, R)
        ST[node] = max(ST[node * 2], ST[node * 2 + 1])


def update(node, L, R, idx, val):
    global A, ST
    if (L == R):
        A[idx] = val
        ST[node] = val

    else:
        mid = (L + R) // 2
        if (L <= idx and idx <= mid):
            update(2 * node, L, mid, idx, val)
        else:
            update(2 * node + 1, mid + 1, R, idx, val)
        ST[node] = max(ST[2 * node], ST[2 * node + 1])


def query(node, L, R, x, l):
    if R < l or ST[node] < x:
        return -1
    if L == R:
        return L if L >= l and A[L] >= x else -1
    mid = (L + R) // 2
    res = query(2 * node, L, mid, x, l)
    if res != -1:
        return res
    return query(2 * node + 1, mid + 1, R, x, l)


n, m = list(map(int, stdin.readline().split()))
A = list(map(int, stdin.readline().split()))
ST = [0 for _ in range(4 * n)]
result = []
build(1, 0, n - 1)
for i in range(m):
    operation = list(map(int, stdin.readline().split()))
    if operation[0] == 1:
        update(1, 0, n - 1, operation[1], operation[2])
    else:
        result.append(query(1, 0, n - 1, operation[1], operation[2]))
print(*result, sep='\n')
