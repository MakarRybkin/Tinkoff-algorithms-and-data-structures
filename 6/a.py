from collections import defaultdict, deque
from sys import  stdin, stdout

N, M = map(int, stdin.readline().split())
edges = defaultdict(list)


for _ in range(M):
    u, v = map(int, stdin.readline().split())
    edges[u].append(v)
print(edges)
def getComponents(N, edges):
    comps = []
    visited = set()

    for node in range(1, N + 1):
        if node in visited:
            continue
        q = deque([node])
        visited.add(node)
        cur_comp = {node}

        while q:
            u = q.popleft()
            for v in edges.get(u, []):
                if v not in visited:
                    q.append(v)
                    visited.add(v)
                    cur_comp.add(v)

        comps.append(sorted(cur_comp))
    return comps

result = getComponents(N, edges)
print(len(result))
for comp in result:
    print(len(comp))
    print(*comp)
