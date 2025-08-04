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
        ST[node] = ST[2 * node] + ST[2 * node + 1]


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
        ST[node] = ST[2 * node] + ST[2 * node + 1]


def query(node, tl, tr, l, r):
    global A, ST
    if (r < tl or tr < l):
        return 0
    if (l <= tl and tr <= r):
        return ST[node]
    tm = (tl + tr) // 2
    return query(2 * node, tl, tm, l, r) + query(2 * node + 1, tm + 1, tr, l, r)

n,m=list(map(int,stdin.readline().split()))
A = list(map(int, stdin.readline().split()))
ST = [0 for _ in range(4 * n)]
result=[]
build(1, 0, n - 1)
for i in range(m):
    operation = list(map(int,stdin.readline().split()))
    if operation[0] == 1:
        update(1,0,n-1,operation[1],operation[2])
    else:
        result.append(query(1,0,n-1,operation[1],operation[2]-1))
print(*result,sep='\n')