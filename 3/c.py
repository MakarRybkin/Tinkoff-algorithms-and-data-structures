# from sys import stdin
# import sys
# sys.setrecursionlimit(10000)
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.children = []
#
# def findPath(root, path, k):
#     # Baes Case
#     if root is None:
#         return False
#
#     path.append(root)
#
#     if (root.data == k or
#             [j for j in list(map(lambda child: findPath(child, path, k), root.children))]!=[False]*(len(root.children))):
#         return True
#
#     path.pop()
#     return False
#
#
# def lca(root, n1, n2):
#     path1 = []
#     path2 = []
#
#     if (not findPath(root, path1, n1) or not findPath(root, path2, n2)):
#         return None
#
#     i = 0
#     while (i < len(path1) and i < len(path2)):
#         if path1[i] != path2[i]:
#             break
#         i += 1
#     return path1[i - 1]
#
#
# if __name__ == '__main__':
#
#     n=int(stdin.readline())
#     p=[int(x) for x in stdin.readline().split()]
#     m=int(stdin.readline())
#     requests=[]
#     for i in range(m):
#         requests.append([int(x) for x in stdin.readline().split()])
#     nodes=[]
#     root = Node(0)
#     nodes.append(root)
#     for i in range(n-1):
#         k=Node(i+1)
#         nodes.append(k)
#         for node in nodes:
#             if node.data == p[i]:
#                 node.children.append(k)
#     for req in requests:
#         ans = lca(root, req[0], req[1])
#         if (ans == None):
#             print("No common ancestor found")
#         else:
#             print(ans.data)
from sys import stdin


class Node:
    def __init__(self, data):
        self.data = data
        self.children = []


def build_tree(n, p):
    nodes = [Node(i) for i in range(n)]
    root = nodes[0]
    for i in range(1, n):
        nodes[p[i - 1]].children.append(nodes[i])
    return root


def find_parent(root, parent_map):
    stack = [root]
    while stack:
        node = stack.pop()
        for child in node.children:
            parent_map[child.data] = node.data
            stack.append(child)


def lca(n1, n2, parent_map):
    ancestors = set()
    while n1 != -1:
        ancestors.add(n1)
        n1 = parent_map.get(n1, -1)
    while n2 != -1:
        if n2 in ancestors:
            return n2
        n2 = parent_map.get(n2, -1)
    return None


if __name__ == '__main__':
    n = int(stdin.readline())
    p = list(map(int, stdin.readline().split()))
    b = int(stdin.readline())
    requests = [list(map(int, stdin.readline().split())) for _ in range(b)]

    parent_map = {}
    root = build_tree(n, p)
    find_parent(root, parent_map)

    for n1, n2 in requests:
        ans = lca(n1, n2, parent_map)
        if ans is None:
            print("No common ancestor found")
        else:
            print(ans)
