from sys import stdin
n,m = [int(x) for x  in stdin.readline().split()]
dp = [[0 for i in range(m)]for j in range(n)]
if n == 0 or m == 0:
    print(0)
    exit()
dp[0][0] = 1
counter = 0
i,j=0,0
for _ in range(n*m ):
        if i>=2 and j>=1:
            dp[i][j] += dp[i-2][j-1]
        if i>=1 and j>=2:
            dp[i][j] += dp[i-1][j-2]
        if i>=2 and j<=m-2:
            dp[i][j] += dp[i-2][j+1]
        if i<=n-2 and j>=1:
            dp[i][j] += dp[i+1][j-2]
        if i == 0 or j == m-1:
            i+=j+1
            if i >= n - counter :
                counter += 1
                i=n-1
                j= counter
            else:
                j=0
        else:
            j+=1
            i-=1
print(dp[-1][-1])