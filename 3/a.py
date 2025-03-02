from sys import stdin
def dfs(tree, start):
    visited = set()
    stack = [(start, 0)]

    maxDistance = 0
    further = start

    while stack:
        node, distance = stack.pop()
        if node not in visited:
            visited.add(node)
            if distance > maxDistance:
                maxDistance = distance
                further = node

            for child in tree[node]:
                stack.append((child, distance + 1))

    return further, maxDistance

def diameter(tree):
    startNode = next(iter(tree))
    further, _ = dfs(tree, startNode)
    _, diameter = dfs(tree, further)
    return diameter

n = int(stdin.readline())
p = [int(x) for x  in stdin.readline().split()]
currNum = 0
h = {currNum: 0}
tree = {0: []}
heights = [0]
max_height = 0
for i in range(n - 1):
    currNum += 1
    if p[i] in tree:
        tree[p[i]].append(currNum)
    else:
        tree[p[i]] = [currNum]
    if currNum in tree:
        tree[currNum].append(p[i])
    else:
        tree[currNum] = [p[i]]

    height_i = h[p[i]] + 1
    h[currNum] = height_i
    heights.append(height_i)
    max_height = max(max_height, height_i)

D = diameter(tree)

print(max_height, D)
print(*heights)