from sys import stdin
n,m=[int(x) for x in stdin.readline().split()]
matrix = []
for i in range(n):
    matrix.append([int(x) for x in stdin.readline().split()])
dp = [[0 for x in range(m+1)] for y in range(n+1)]
max_squere=0
coords = [0,0]
for i in range(0,n):
    for j in range(0,m):
        if matrix[i][j] == 1:
            dp[i+1][j+1] = min(dp[i][j+1]+1, dp[i+1][j]+1, dp[i][j]+1)
            if max_squere <= dp[i+1][j+1]:
                max_squere = dp[i+1][j+1]
                coords = [i-max_squere+2,j-max_squere+2]
print(max_squere)
print(*coords)

