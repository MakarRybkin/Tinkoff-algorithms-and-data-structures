from sys import stdin, stdout

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.size = 4 * n
        self.tree = [0] * self.size
        self.lazy = [0] * self.size

    def _push(self, node, l, r):
        if self.lazy[node] != 0:
            self.tree[node] += self.lazy[node]
            if r  > l + 1:
                self.lazy[node * 2] += self.lazy[node]
                self.lazy[node * 2 + 1] += self.lazy[node]
            self.lazy[node] = 0

    def add(self, node, l, r, ql, qr, v):
        self._push(node, l, r)
        if qr <= l or r <= ql:
            return
        if ql <= l and r <= qr:
            self.lazy[node] += v
            self._push(node, l, r)
        else:
            m = (l + r) // 2
            self.add(node * 2, l, m, ql, qr, v)
            self.add(node * 2 + 1, m, r, ql, qr, v)
            self.tree[node] = min(self.tree[node * 2], self.tree[node * 2 + 1])

    def sum(self, node, l, r, ql, qr):
        self._push(node, l, r)
        if qr <= l or r <= ql:
            return 0
        if ql <= l and r <= qr:
            return self.tree[node]
        m = (l + r) // 2
        left = self.sum(node * 2, l, m, ql, qr)
        right = self.sum(node * 2 + 1, m, r, ql, qr)
        return min(left, right)


n, m = [int(x) for x in stdin.readline().split()]
st = SegmentTree(n)
res = []
for i in range(m):
    parts = [int(x) for x in stdin.readline().split()]
    if parts[0] == 1:
        st.add(1,0, st.n, parts[1], parts[2], parts[3])
    else:
        res.append(str(st.sum(1, 0, st.n, parts[1], parts[2])))
print(*res,sep='\n')
