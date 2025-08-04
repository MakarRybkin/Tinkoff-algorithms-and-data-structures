from sys import stdin
from bisect import bisect_left

class SimpleSegmentTree:
    def build(self, node, L, R):
        if L == R:
            self.ST[node] = self.A[L]
        else:
            mid = (L + R) // 2
            self.build(2 * node, L, mid)
            self.build(2 * node + 1, mid + 1, R)
            self.ST[node] = self.operation(self.ST[2 * node], self.ST[2 * node + 1])

    def __init__(self, size):
        self.n = size
        self.A = [0] * size
        self.neutral = 0
        self.ST = [0] * (4 * self.n)
        self.build(1, 0, self.n - 1)

    def operation(self, x, y):
        return x + y

    def query(self, l, r):
        return self.query_internal(1, 0, self.n - 1, l, r)

    def update(self, idx, val):
        return self.update_internal(1, 0, self.n - 1, idx, val)

    def update_internal(self, node, L, R, idx, val):
        if L == R:
            self.A[idx] += val
            self.ST[node] += val
        else:
            mid = (L + R) // 2
            if idx <= mid:
                self.update_internal(2 * node, L, mid, idx, val)
            else:
                self.update_internal(2 * node + 1, mid + 1, R, idx, val)
            self.ST[node] = self.operation(self.ST[2 * node], self.ST[2 * node + 1])

    def query_internal(self, node, tl, tr, l, r):
        if r < tl or tr < l:
            return self.neutral
        if l <= tl and tr <= r:
            return self.ST[node]
        tm = (tl + tr) // 2
        return self.operation(
            self.query_internal(2 * node, tl, tm, l, r),
            self.query_internal(2 * node + 1, tm + 1, tr, l, r)
        )


n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))

sorted_a = sorted(set(a))
a_comp = [bisect_left(sorted_a, x) for x in a]
max_val = len(sorted_a)

left = [0] * n
tree = SimpleSegmentTree(max_val)
for i in range(n):
    left[i] = tree.query(a_comp[i] + 1, max_val - 1)
    tree.update(a_comp[i], 1)

right = [0] * n
tree = SimpleSegmentTree(max_val)
for i in reversed(range(n)):
    right[i] = tree.query(0, a_comp[i] - 1)
    tree.update(a_comp[i], 1)

ans = sum(left[i] * right[i] for i in range(n))
print(ans)
