import sys
sys.setrecursionlimit(1 << 25)

class SegmentTreeNode:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.left = None
        self.right = None
        self.lazy = None
        self.black_len = 0
        self.black_segments = 0
        self.left_color = 'W'
        self.right_color = 'W'

class SegmentTree:
    def __init__(self, coords):
        self.coords = coords
        self.root = self.build(0, len(coords) - 1)

    def build(self, l, r):
        node = SegmentTreeNode(l, r)
        if r - l > 1:
            m = (l + r) // 2
            node.left = self.build(l, m)
            node.right = self.build(m, r)
        return node

    def apply(self, node, color):
        l = self.coords[node.l]
        r = self.coords[node.r]
        if color == 'B':
            node.black_len = r - l
            node.black_segments = 1
            node.left_color = node.right_color = 'B'
        else:
            node.black_len = 0
            node.black_segments = 0
            node.left_color = node.right_color = 'W'
        if node.left:
            node.lazy = color

    def push(self, node):
        if node.lazy and node.left:
            self.apply(node.left, node.lazy)
            self.apply(node.right, node.lazy)
            node.lazy = None

    def pull(self, node):
        node.black_len = node.left.black_len + node.right.black_len
        node.black_segments = node.left.black_segments + node.right.black_segments
        if node.left.right_color == 'B' and node.right.left_color == 'B':
            node.black_segments -= 1
        node.left_color = node.left.left_color
        node.right_color = node.right.right_color

    def update(self, node, l, r, color):
        if self.coords[node.r] <= l or self.coords[node.l] >= r:
            return
        if l <= self.coords[node.l] and self.coords[node.r] <= r:
            self.apply(node, color)
            return
        self.push(node)
        self.update(node.left, l, r, color)
        self.update(node.right, l, r, color)
        self.pull(node)

    def query(self):
        return self.root.black_segments, self.root.black_len

n = int(sys.stdin.readline())
ops = []
coords = set()
for _ in range(n):
    parts = sys.stdin.readline().split()
    c = parts[0]
    x = int(parts[1])
    l = int(parts[2])
    ops.append((c, x, x + l))
    coords.add(x)
    coords.add(x + l)

sorted_coords = sorted(coords)
coord_map = {v: i for i, v in enumerate(sorted_coords)}
tree = SegmentTree(sorted_coords)

for c, x1, x2 in ops:
    tree.update(tree.root, x1, x2, c)
    segs, total = tree.query()
    print(segs, total)

