import math

t = int(input())

for _ in range(t):
    n, b = map(int, input().split())
    nm = n * b
    best = 1e18
    ax = 'V'
    res = 0
    total_sum = nm * (nm + 1) // 2

    split = int((math.sqrt(nm * nm + b * b + 2 * nm + 1) - nm + b - 1) // 2)

    for i in range(split, min(b, split + 1) + 1):
        s = i * n * (i + 1 + nm - b) // 2
        diff = abs(s - (total_sum - s))
        if best > diff:
            best = diff
            ax = 'V'
            res = i

    split = int((math.sqrt(2 * nm * nm + 2 * nm + 1) - 1) // 2 // b)

    for i in range(split, min(n, split + 1) + 1):
        s = (b * b * i * i + b * i) // 2
        diff = abs(s - (total_sum - s))
        if best > diff:
            best = diff
            ax = 'H'
            res = i

    print(ax, res + 1)





