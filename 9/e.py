import sys
sys.setrecursionlimit(10**8)

class SegmentTree:
    def __init__(self, coords):
        self.n = len(coords) - 1
        self.tree = [0] * (self.n * 4)
        self.cover = [0] * (self.n * 4)
        self.coords = coords

    def _update(self, node, l, r, ul, ur, val):
        if ur < l or r < ul:
            return
        if ul <= l and r <= ur:
            self.cover[node] += val
        else:
            m = (l + r) // 2
            self._update(node * 2, l, m, ul, ur, val)
            self._update(node * 2 + 1, m + 1, r, ul, ur, val)
        if self.cover[node] > 0:
            self.tree[node] = self.coords[r + 1] - self.coords[l]
        else:
            if l == r:
                self.tree[node] = 0
            else:
                self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def update(self, x1, x2, val):
        self._update(1, 0, self.n - 1, x1, x2 - 1, val)

    def query(self):
        return self.tree[1]

def coordinate_compress(xs):
    xs_sorted = sorted(set(xs))
    mapping = {x: i for i, x in enumerate(xs_sorted)}
    return mapping, xs_sorted

n = int(sys.stdin.readline())
events = []
xs = []

for _ in range(n):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    if x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1
        events.append((y1, +1, x1, x1 + 1))
        events.append((y2 + 1, -1, x1, x1 + 1))
        xs.extend([x1, x1 + 1])
    else:
        if x1 > x2:
            x1, x2 = x2, x1
        events.append((y1, +1, x1, x2 + 1))
        events.append((y1 + 1, -1, x1, x2 + 1))
        xs.extend([x1, x2 + 1])

x_map, x_list = coordinate_compress(xs)
st = SegmentTree(x_list)
events.sort()

prev_y = events[0][0]
total = 0

for y, typ, x1, x2 in events:
    dy = y - prev_y
    total += st.query() * dy
    st.update(x_map[x1], x_map[x2], typ)
    prev_y = y

print(total)

