from sys import stdin
class DisjSet:
    def __init__(self, n):
        self.rank = [1] * n
        self.size = [1] * n
        self.min = [i for i in range(n)]
        self.max = [i for i in range(n)]
        self.parent = [i for i in range(n)]

    def find(self, x):
        if (self.parent[x] != x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]



    def getSize(self, x):
        return self.size[self.find(x)]
    def getMin(self, x):
        return self.min[self.find(x)]
    def getMax(self, x):
        return self.max[self.find(x)]

    def Union(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
        if xset == yset:
            return
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] = self.rank[xset] + 1
        pset = self.find(x)
        self.min[pset] = min(self.min[xset], self.min[yset])
        self.max[pset] = max(self.max[xset], self.max[yset])
        self.size[pset] = (self.size[xset] + self.size[yset])

n,m = [int(x) for x in stdin.readline().split()]
dsu = DisjSet(n+1)
result = []
for i in range(m):
    operation = stdin.readline().split()
    if operation[0] == 'union':
        dsu.Union(int(operation[1]), int(operation[2]))
    else:
        result.append([dsu.getMin(int(operation[1])),dsu.getMax(int(operation[1])),dsu.getSize(int(operation[1]))])
[print(*i) for i in result]