from sys import stdin
s= stdin.readline().strip()
def valid_bracket_sequence(s):
    n = len(s)
    dp = [["" for _ in range(n)] for _ in range(n)]
    parentheses = {'(':')','[':']','{':'}'}
    def is_match(opening, closing):
        if opening in parentheses.keys():
            return parentheses[opening] == closing
        return False

    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if is_match(s[i], s[j]):
                dp[i][j] = s[i] + dp[i + 1][j - 1] + s[j]
            for k in range(i, j):
                if len(dp[i][k] + dp[k + 1][j]) > len(dp[i][j]):
                    dp[i][j] = dp[i][k] + dp[k + 1][j]

    return dp[0][n - 1]


print(valid_bracket_sequence(s))

