# import sys
# from bisect import bisect_left, bisect_right
# sys.setrecursionlimit(10**8)
# input = sys.stdin.readline
#
# class SegmentTree:
#     def __init__(self, size):
#         self.size = size
#         self.tree = [0] * (4 * size)
#         self.lazy = [-float('inf')] * (4 * size)
#
#     def push(self, v, tl, tr):
#         if self.lazy[v] != -float('inf'):
#             self.tree[v] = max(self.tree[v], self.lazy[v])
#
#             if tl != tr:
#                 self.lazy[2*v] = max(self.lazy[2*v], self.lazy[v])
#                 self.lazy[2*v+1] = max(self.lazy[2*v+1], self.lazy[v])
#
#             self.lazy[v] = -float('inf')
#
#     def update_range(self, v, tl, tr, l, r, new_value):
#         self.push(v, tl, tr)
#
#         if l > r or tl > tr or l > tr or r < tl:
#             return
#
#         if l <= tl and tr <= r:
#             self.tree[v] = max(self.tree[v], new_value)
#             self.lazy[v] = max(self.lazy[v], new_value)
#             return
#
#         tm = (tl + tr) // 2
#         self.update_range(2*v, tl, tm, l, min(r, tm), new_value)
#         self.update_range(2*v+1, tm+1, tr, max(l, tm+1), r, new_value)
#         self.tree[v] = max(self.tree[2*v], self.tree[2*v+1])
#
#     def query_range(self, v, tl, tr, l, r):
#         self.push(v, tl, tr)
#
#         if l > r or tl > tr or l > tr or r < tl:
#             return -float('inf')
#
#         if l <= tl and tr <= r:
#              return self.tree[v]
#
#         tm = (tl + tr) // 2
#         left_max = self.query_range(2*v, tl, tm, l, min(r, tm))
#         right_max = self.query_range(2*v+1, tm+1, tr, max(l, tm+1), r)
#         return max(left_max, right_max)
#
#     def query_point(self, y_index):
#         return self.query_range(1, 0, self.size - 1, y_index, y_index)
#
# line_parts = input().split()
# w_orig = int(line_parts[0])
# h_orig = int(line_parts[1])
# n = int(line_parts[2])
#
# centers_input = []
# for i in range(n):
#     x_double, y_double = map(float, input().split())
#     centers_input.append({'x': int(x_double * 2), 'y': int(y_double * 2), 'id': i})
#
# all_y_coords = [c['y'] for c in centers_input]
# unique_y = sorted(list(set(all_y_coords)))
# m = len(unique_y)
#
# segment_tree = SegmentTree(m)
#
# centers_sorted_by_x = sorted(centers_input, key=lambda c: c['x'])
#
# ans = [0] * n
#
# for center in centers_sorted_by_x:
#     y_index = bisect_left(unique_y, center['y'])
#
#     max_boundary = segment_tree.query_point(y_index)
#
#     S_original = center['x'] - max_boundary
#
#     S_original = max(1, S_original)
#
#     ans[center['id']] = S_original
#
#     first_y_index_to_update = bisect_left(unique_y, center['y'] - S_original)
#     after_y_index_to_update = bisect_right(unique_y, center['y'] + S_original)
#
#     update_value = center['x'] + S_original
#
#     segment_tree.update_range(1, 0, m - 1, first_y_index_to_update, after_y_index_to_update - 1, update_value)
#
# for value in ans:
#     print(value,end=' ')
import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

class IterativeSegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (2 * size)

    def update_range(self, l, r, value):
        """Обновить [l, r] включительно: установить максимум"""
        l += self.size
        r += self.size
        while l <= r:
            if l % 2 == 1:
                self.tree[l] = max(self.tree[l], value)
                l += 1
            if r % 2 == 0:
                self.tree[r] = max(self.tree[r], value)
                r -= 1
            l //= 2
            r //= 2

    def query_point(self, pos):
        """Запросить максимум в точке pos"""
        pos += self.size
        res = self.tree[pos]
        while pos > 1:
            pos //= 2
            res = max(res, self.tree[pos])
        return res

# Чтение входа
w_orig, h_orig, n = map(int, input().split())
centers_input = []

for i in range(n):
    x, y = map(float, input().split())
    centers_input.append((int(x * 2), int(y * 2), i))

# Уникальные y
all_y = [y for _, y, _ in centers_input]
unique_y = sorted(set(all_y))
y_to_index = {y: i for i, y in enumerate(unique_y)}
m = len(unique_y)

# Новое дерево
segment_tree = IterativeSegmentTree(m)

# Сортировка по x
centers_sorted_by_x = sorted(centers_input, key=lambda c: c[0])

ans = [0] * n

for x, y, idx in centers_sorted_by_x:
    y_idx = y_to_index[y]
    max_b = segment_tree.query_point(y_idx)
    S = max(1, x - max_b)

    ans[idx] = S

    l_val = y - S
    r_val = y + S
    l_idx = bisect_left(unique_y, l_val)
    r_idx = bisect_right(unique_y, r_val) - 1

    segment_tree.update_range(l_idx, r_idx, x + S)

for value in ans:
    print(value,end=' ')
