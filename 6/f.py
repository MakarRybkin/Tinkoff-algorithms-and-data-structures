from collections import defaultdict, deque
from sys import stdin

m = int(stdin.readline())
edges = defaultdict(list)
for i in range(m):
    elements = list(stdin.readline().split())
    parent, child = elements[0], elements[-1]
    edges[parent].append(child)
first_element = stdin.readline().strip()
last_element = stdin.readline().strip()


def bfs(edges):
    queue = deque()
    visited = {}
    time = 0
    min_time = 10 ** 9
    queue.append((first_element, time))
    while queue:
        element = queue.popleft()
        if element[0] == last_element:
            min_time = min(min_time, element[1])
        if element not in visited:
            visited[element[0]] = element[1]
            for child in edges[element[0]]:
                if child not in visited:
                    queue.append((child, visited[element[0]] + 1))
    if min_time < 10 ** 9:
        return min_time
    else:
        return -1


print(bfs(edges))
