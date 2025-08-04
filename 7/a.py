from sys import stdin
n= int(stdin.readline())
stairs = [int(x) for x in stdin.readline().split()]
dp= [0] * n
dp[0] = stairs[0]
if n >1:
    dp[1] = stairs[1]
for i in range(2, n):
    dp[i] = min(dp[i-1] + stairs[i], dp[i-2] + stairs[i])
print(dp[-1])