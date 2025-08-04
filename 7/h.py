from sys import stdin

n = int(stdin.readline())
sequence = list(map(int, stdin.readline().split()))
dp = [1] * n
prev = [-1] * n

for i in range(n):
    for j in range(i):
        if sequence[j] < sequence[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            prev[i] = j

max_length = max(dp)
index = dp.index(max_length)

lis = []
while index != -1:
    lis.append(sequence[index])
    index = prev[index]
lis.reverse()
print(max_length)
print(*lis)
