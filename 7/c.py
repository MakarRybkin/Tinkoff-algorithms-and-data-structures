# from sys import stdin
# n, k = [int(x) for x in stdin.readline().split()]
# steps = [0] + [int(x) for x in stdin.readline().split()] + [0]
# dp = [-1] * (n )
# dp[0] = steps[0]
# prev_indices = [-1] * (n )
#
# for i in range(1, n):
#     dp[i] = dp[i - 1] + steps[i]
#     for j in range(i - 1 , max(-1, i - k -1), -1):
#         if dp[j] + steps[i] >= dp[i]:
#             dp[i] = dp[j] + steps[i]
#             prev_indices[i] = j
#
# path = []
# i = n - 1
# while i != -1:
#     path.append(i + 1)
#     i = prev_indices[i]
# path = path[::-1]
# print(dp[-1])
# print(len(path)-1)
# print(*path)
from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
coins_input = list(map(int, stdin.readline().split()))
coins = [0] + coins_input + [0]
dp = [-float('inf')] * n
prev = [-1] * n
dp[0] = 0

dq = deque()
dq.append(0)

for i in range(1, n):

    while dq and dq[0] < i - k:
        dq.popleft()

    dp[i] = dp[dq[0]] + coins[i]
    prev[i] = dq[0]

    while dq and dp[dq[-1]] <= dp[i]:
        dq.pop()

    dq.append(i)

path = []
pos = n - 1
while pos != -1:
    path.append(pos + 1)
    pos = prev[pos]
path.reverse()

print(dp[n - 1])
print(len(path) - 1)
print(*path)


