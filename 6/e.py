from collections import deque
from sys import stdin, stdout

def min_sum_digits(N):
    graph = [[] for _ in range(N)]

    for i in range(1, N + 1):
        frm = i % N
        to = (i + 1) % N
        graph[frm].append((to, 1))

    for i in range(1, N + 1):
        frm = i % N
        to = (10 * i) % N
        graph[frm].append((to, 0))

    inf = int(1e9)
    distance = [inf] * N
    distance[1] = 0
    dq = deque([1])

    while dq:
        current = dq.popleft()

        for neighbor, weight in graph[current]:
            if distance[neighbor] > distance[current] + weight:
                distance[neighbor] = distance[current] + weight
                if weight == 0:
                    dq.appendleft(neighbor)
                else:
                    dq.append(neighbor)

    print(1 + distance[0])


N = int(stdin.readline())
min_sum_digits(N)











