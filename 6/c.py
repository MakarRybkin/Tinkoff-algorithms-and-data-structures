from collections import defaultdict
import sys


def is_topological_sort(n, edges, check):

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    position = {node: i for i, node in enumerate(check)}

    for u in range(1, n + 1):
        for v in graph[u]:
            if position[u] > position[v]:
                return "NO"

    return "YES"


n, m = map(int, sys.stdin.readline().split())
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
check = list(map(int, sys.stdin.readline().split()))

print(is_topological_sort(n, edges, check))
