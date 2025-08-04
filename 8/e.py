from sys import stdin
MOD = 10 ** 9 + 7
A = []
ST = []

def build(node, L, R):
    global ST
    ST[node] = (0, 0)

def update(node, L, R, idx, val):
    if L == R:
        curr_len, curr_cnt = ST[node]
        new_len, new_cnt = val
        if new_len > curr_len:
            ST[node] = (new_len, new_cnt % MOD)
        elif new_len == curr_len:
            ST[node] = (curr_len, (curr_cnt + new_cnt) % MOD)
    else:
        mid = (L + R) // 2
        if idx <= mid:
            update(2 * node, L, mid, idx, val)
        else:
            update(2 * node + 1, mid + 1, R, idx, val)

        left = ST[2 * node]
        right = ST[2 * node + 1]
        if left[0] > right[0]:
            ST[node] = left
        elif right[0] > left[0]:
            ST[node] = right
        else:
            ST[node] = (left[0], (left[1] + right[1]) % MOD)

def query(node, L, R, l, r):
    if r < L or R < l:
        return (0, 0)
    if l <= L and R <= r:
        return ST[node]
    mid = (L + R) // 2
    left = query(2 * node, L, mid, l, r)
    right = query(2 * node + 1, mid + 1, R, l, r)
    if left[0] > right[0]:
        return left
    elif right[0] > left[0]:
        return right
    else:
        return (left[0], (left[1] + right[1]) % MOD)

n = int(stdin.readline())
A = list(map(int, stdin.readline().split()))

sorted_unique = sorted(set(A))
compressed = {v: i for i, v in enumerate(sorted_unique)}
A = [compressed[x] for x in A]
size = len(sorted_unique)

ST = [(0, 0) for _ in range(4 * size)]
build(1, 0, size - 1)

for val in A:
    if val == 0:
        maxlen, cnt = 0, 1
    else:
        maxlen, cnt = query(1, 0, size - 1, 0, val - 1)
        if cnt == 0:
            cnt = 1
    update(1, 0, size - 1, val, (maxlen + 1, cnt))

max_len, total_cnt = query(1, 0, size - 1, 0, size - 1)
print(total_cnt % MOD)
