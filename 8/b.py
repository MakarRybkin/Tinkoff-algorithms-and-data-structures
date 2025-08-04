from sys import stdin


A = []
ST = []


def build(node, L, R):
    global A, ST
    if (L == R):
        ST[node] = [A[L],1]

    else:

        mid = (L + R) // 2
        build(2 * node, L, mid)
        build(2 * node + 1, mid + 1, R)
        counter=0
        if ST[2*node][0]==ST[2*node+1][0]:
            counter=ST[2*node][1]+ST[2*node+1][1]
        elif ST[2*node][0]<ST[2*node+1][0]:
            counter=ST[2*node][1]
        else:
            counter=ST[2*node+1][1]
        ST[node] = [min(ST[2 * node][0], ST[2 * node + 1][0]),counter]


def update(node, L, R, idx, val):
    global A, ST
    if (L == R):
        A[idx] = val
        ST[node] = [val,1]

    else:
        mid = (L + R) // 2
        if (L <= idx and idx <= mid):
            update(2 * node, L, mid, idx, val)
        else:
            update(2 * node + 1, mid + 1, R, idx, val)
        if ST[2 * node][0] == ST[2 * node + 1][0]:
            counter = ST[2 * node][1] + ST[2 * node + 1][1]
        elif ST[2 * node][0] < ST[2 * node + 1][0]:
            counter = ST[2 * node][1]
        else:
            counter = ST[2 * node + 1][1]
        ST[node] = [min(ST[2 * node][0], ST[2 * node + 1][0]), counter]


def query(node, tl, tr, l, r):
    if r < tl or tr < l:
        return [10 ** 10, 0]
    if l <= tl and tr <= r:
        return ST[node]

    tm = (tl + tr) // 2
    left = query(2 * node, tl, tm, l, r)
    right = query(2 * node + 1, tm + 1, tr, l, r)

    if left[0] == right[0]:
        return [left[0], left[1] + right[1]]
    elif left[0] < right[0]:
        return left
    else:
        return right

n,m=list(map(int,stdin.readline().split()))
A = list(map(int, stdin.readline().split()))
ST = [[0,1] for _ in range(4 * n)]
result=[]
build(1, 0, n - 1)
for i in range(m):
    operation = list(map(int,stdin.readline().split()))
    if operation[0] == 1:
        update(1,0,n-1,operation[1],operation[2])
    else:
        result.append(query(1,0,n-1,operation[1],operation[2]-1))
[print(*r) for r  in result]
