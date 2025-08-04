import sys
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cells):
    visited[x][y] = True
    cells.append(grid[x][y])
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if grid[nx][ny] in ['#', 'X']:
                dfs(nx, ny, cells)

whole = damaged = destroyed = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j] and grid[i][j] in ['#', 'X']:
            cells = []
            dfs(i, j, cells)
            cell_set = set(cells)
            if cell_set == {'#'}:
                whole += 1
            elif cell_set == {'X'}:
                destroyed += 1
            else:
                damaged += 1

print(whole, damaged, destroyed)
