
from sys import stdin


def build_prefix_sum(matrix, n, m):
    prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            prefix_sum[i][j] = (matrix[i - 1][j - 1] +
                                prefix_sum[i - 1][j] +
                                prefix_sum[i][j - 1] -
                                prefix_sum[i - 1][j - 1])
    return prefix_sum


def count_sum(prefix_sum, x1, y1, x2, y2):
    return (prefix_sum[x2][y2] -
            prefix_sum[x1 - 1][y2] -
            prefix_sum[x2][y1 - 1] +
            prefix_sum[x1 - 1][y1 - 1])


data = stdin.readlines()
n, b, k = map(int, data[0].split())

matrix = []
for i in range(1, n + 1):
    row = list(map(int, data[i].split()))
    matrix.append(row)

prefix_sum = build_prefix_sum(matrix, n, b)

for i in range(k):
    x1, y1, x2, y2 = map(int, data[n + 1 + i].split())
    print(count_sum(prefix_sum, x1, y1, x2, y2))
