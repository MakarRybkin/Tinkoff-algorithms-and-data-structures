import sys
from sys import stdin
from collections import defaultdict

sys.setrecursionlimit(1000000)

def has_cycle(v):
    color[v] = 'gray'
    for neighbor in graph[v]:
        if color[neighbor] == 'gray':
            return True
        if color[neighbor] == 'white' and has_cycle(neighbor):
            return True
    color[v] = 'black'
    return False

n, m = map(int, stdin.readline().split())
graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)

color = {i: 'white' for i in range(1, n + 1)}

for i in range(1, n + 1):
    if color[i] == 'white' and has_cycle(i):
        print(1)
        exit()

print(0)
