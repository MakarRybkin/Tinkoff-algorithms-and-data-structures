from collections import defaultdict, deque
from sys import stdin, stdout

N, M = map(int, stdin.readline().split())
edges = defaultdict(list)

for i in range(M):
    frm, to, weight = map(int, stdin.readline().split())
    edges[frm].append((to, weight))
    edges[to].append((frm, weight))


def bfs(edges, root):
    weights = {}
    queue = deque()
    visited = {}
    queue.append((root, 0))

    while queue:
        frm, weight = queue.popleft()
        if frm in visited and weight >= visited[frm]:
            continue
        visited[frm] = weight
        weights[frm] = weight

        for child in edges[frm]:
            child_node, child_weight = child
            if child_node not in visited or weight + child_weight < visited[child_node]:
                queue.append((child_node, weight + child_weight))

    return max(weights.values()) if weights else float('inf')


path_max = float('inf')
res = -1

for root in edges.keys():
    root_max_path = bfs(edges, root)
    if root_max_path < path_max:
        path_max = root_max_path
        res = root

print(res)