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


def update(node, L, R, idx):
    global A, ST
    rev = {0:1,1:0}
    if (L == R):
        A[idx] = rev[A[idx]]
        ST[node] = A[idx]

    else:
        mid = (L + R) // 2
        if (L <= idx and idx <= mid):
            update(2 * node, L, mid, idx)
        else:
            update(2 * node + 1, mid + 1, R, idx)
        ST[node] = ST[2 * node] + ST[2 * node + 1]


def query(node, L, R, k):
    if L == R:
        return L
    mid = (L + R) // 2
    if ST[2 * node] > k:
        return query(2 * node, L, mid, k)
    else:
        return query(2 * node + 1, mid + 1, R, k - ST[2 * node])

n,m=list(map(int,stdin.readline().strip().split()))
A = list(map(int, stdin.readline().split()))
ST = [0 for _ in range(4 * n)]
res = 0
result=[]
build(1, 0, n - 1)
for i in range(m):
    operation = list(map(int,stdin.readline().split()))
    if operation[0] == 1:
        update(1,0,n-1,operation[1])
    else:
        result.append(query(1,0,n-1,operation[1]))
print(*result,sep='\n')