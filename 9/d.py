import sys

sys.setrecursionlimit(1 << 25)

class SegmentTree:
    def __init__(self, y_values):
        self.size = len(y_values)
        self.N = 1
        while self.N < self.size:
            self.N <<= 1
        self.tree = [0] * (2 * self.N)
        self.lazy = [0] * (2 * self.N)
        self.max_pos = [0] * (2 * self.N)
        self.y_map = [0] * (2 * self.N)
        for i in range(self.size):
            self.max_pos[self.N + i] = i
            self.y_map[self.N + i] = y_values[i]
        for i in range(self.N - 1, 0, -1):
            self._recalc(i)

    def _push(self, v):
        if self.lazy[v]:
            for u in [v * 2, v * 2 + 1]:
                self.tree[u] += self.lazy[v]
                self.lazy[u] += self.lazy[v]
            self.lazy[v] = 0

    def _recalc(self, v):
        left = v * 2
        right = v * 2 + 1
        if self.tree[left] >= self.tree[right]:
            self.tree[v] = self.tree[left]
            self.max_pos[v] = self.max_pos[left]
        else:
            self.tree[v] = self.tree[right]
            self.max_pos[v] = self.max_pos[right]

    def update(self, l, r, value, v=1, tl=0, tr=None):
        if tr is None:
            tr = self.N - 1
        if r < tl or tr < l:
            return
        if l <= tl and tr <= r:
            self.tree[v] += value
            self.lazy[v] += value
            return
        self._push(v)
        tm = (tl + tr) // 2
        self.update(l, r, value, v * 2, tl, tm)
        self.update(l, r, value, v * 2 + 1, tm + 1, tr)
        self._recalc(v)

    def get_max(self):
        return self.tree[1], self.y_map[self.N + self.max_pos[1]]


n = int(sys.stdin.readline())
rectangles = []
y_coords = set()

for _ in range(n):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    rectangles.append((x1, y1, x2, y2))
    y_coords.update([y1, y2])

sorted_y = sorted(y_coords)
y_id = {v: i for i, v in enumerate(sorted_y)}
events = []

for x1, y1, x2, y2 in rectangles:
    events.append((x1, 1, y_id[y1], y_id[y2]))
    events.append((x2 + 1, -1, y_id[y1], y_id[y2]))

events.sort()

st = SegmentTree(sorted_y)
max_cover = 0
max_point = (0, 0)

for x, typ, y1, y2 in events:
    st.update(y1, y2, typ)
    cur_max, y_val = st.get_max()
    if cur_max > max_cover:
        max_cover = cur_max
        max_point = (x, y_val)

print(max_cover)
print(f"{max_point[0]} {max_point[1]}")

