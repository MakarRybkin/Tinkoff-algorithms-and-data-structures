from collections import deque
import sys

moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]


def bfs(n, x1, y1, x2, y2):
    queue = deque([(x1, y1)])
    dist = [[-1] * (n + 1) for _ in range(n + 1)]
    parent = [[None] * (n + 1) for _ in range(n + 1)]

    dist[x1][y1] = 0

    while queue:
        x, y = queue.popleft()

        if (x, y) == (x2, y2):
            path = []
            while True:
                path.append((x, y))
                if parent[x][y] is None:
                    break
                x, y = parent[x][y]
            path.reverse()
            return dist[x2][y2], path

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= n and 1 <= ny <= n and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                parent[nx][ny] = (x, y)
                queue.append((nx, ny))

    return -1, []

n = int(sys.stdin.readline())
x1, y1 = map(int, sys.stdin.readline().split())
x2, y2 = map(int, sys.stdin.readline().split())

count, path = bfs(n, x1, y1, x2, y2)

print(count)
for x, y in path:
    print(x, y)
