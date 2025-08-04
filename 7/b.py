from sys import stdin
n = int(stdin.readline())

def count_safe_stacks(n):
    dp = [[0] * 3 for _ in range(n + 1)]

    dp[1][0] = 1  # A
    dp[1][1] = 1  # B
    dp[1][2] = 1  # C

    for i in range(2, n + 1):
        dp[i][0] = dp[i - 1][1] + dp[i - 1][2]
        dp[i][1] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]
        dp[i][2] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]

    return dp[n][0] + dp[n][1] + dp[n][2]

print(count_safe_stacks(n))

