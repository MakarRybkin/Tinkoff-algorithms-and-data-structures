from sys import stdin, stdout

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
        self.add_lazy = [0] * (4 * n)
        self.set_lazy = [None] * (4 * n)

    def _push(self, node, l, r):
        if self.set_lazy[node] is not None:
            self.tree[node] = (r - l) * self.set_lazy[node]
            if r - l > 1:
                self.set_lazy[node * 2] = self.set_lazy[node]
                self.set_lazy[node * 2 + 1] = self.set_lazy[node]
                self.add_lazy[node * 2] = 0
                self.add_lazy[node * 2 + 1] = 0
            self.set_lazy[node] = None

        if self.add_lazy[node] != 0:
            self.tree[node] += (r - l) * self.add_lazy[node]
            if r - l > 1:
                if self.set_lazy[node * 2] is None:
                    self.add_lazy[node * 2] += self.add_lazy[node]
                else:
                    self.set_lazy[node * 2] += self.add_lazy[node]

                if self.set_lazy[node * 2 + 1] is None:
                    self.add_lazy[node * 2 + 1] += self.add_lazy[node]
                else:
                    self.set_lazy[node * 2 + 1] += self.add_lazy[node]
            self.add_lazy[node] = 0

    def set(self, node, l, r, ql, qr, v):
        self._push(node, l, r)
        if qr <= l or r <= ql:
            return
        if ql <= l and r <= qr:
            self.set_lazy[node] = v
            self.add_lazy[node] = 0
            self._push(node, l, r)
        else:
            m = (l + r) // 2
            self.set(node * 2, l, m, ql, qr, v)
            self.set(node * 2 + 1, m, r, ql, qr, v)
            self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def add(self, node, l, r, ql, qr, v):
        self._push(node, l, r)
        if qr <= l or r <= ql:
            return
        if ql <= l and r <= qr:
            self.add_lazy[node] += v
            self._push(node, l, r)
        else:
            m = (l + r) // 2
            self.add(node * 2, l, m, ql, qr, v)
            self.add(node * 2 + 1, m, r, ql, qr, v)
            self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def sum(self, node, l, r, ql, qr):
        self._push(node, l, r)
        if qr <= l or r <= ql:
            return 0
        if ql <= l and r <= qr:
            return self.tree[node]
        m = (l + r) // 2
        left = self.sum(node * 2, l, m, ql, qr)
        right = self.sum(node * 2 + 1, m, r, ql, qr)
        return left + right


n, m = [int(x) for x in stdin.readline().split()]
st = SegmentTree(n)
res = []
for i in range(m):
    parts = [int(x) for x in stdin.readline().split()]
    if parts[0] == 1:
        st.set(1,0, st.n, parts[1], parts[2], parts[3])
    elif parts[0] == 2:
        st.add(1, 0, st.n, parts[1], parts[2], parts[3])
    elif parts[0] == 3:
        res.append(str(st.sum(1,0,st.n,parts[1],parts[2])))
print(*res,sep='\n')
