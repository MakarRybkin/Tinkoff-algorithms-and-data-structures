from sys import stdin
from functools import cmp_to_key


def comparator(a, b):
    return a[2] - b[2]


def kruskals_mst(V, edges):
    # Sort all edges
    edges = sorted(edges, key=cmp_to_key(comparator))

    # Traverse edges in sorted order
    dsu = DSU(V)
    cost = 0
    count = 0
    for x, y, w in edges:

        # Make sure that there is no cycle
        if dsu.find(x) != dsu.find(y):
            dsu.union(x, y)
            cost += w
            count += 1
            if count == V - 1:
                break
    return cost


# Disjoint set data structure
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.rank[s1] < self.rank[s2]:
                self.parent[s1] = s2
            elif self.rank[s1] > self.rank[s2]:
                self.parent[s2] = s1
            else:
                self.parent[s2] = s1
                self.rank[s1] += 1


n,m = [int(x) for x in stdin.readline().split()]
edges=[]
for i in range(m):
    edges.append([int(x) for x  in stdin.readline().split()])
print(kruskals_mst(n+1, edges))
