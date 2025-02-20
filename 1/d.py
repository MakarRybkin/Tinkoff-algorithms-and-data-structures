import math

def function(x, n):
    return x**2 + math.sqrt(x + 1) - n

def solve(n):
    eps = 1e-10
    low, high = 0.0, n
    while high - low > eps:
        mid = (low + high) / 2
        if function(low, n) * function(mid, n) <= 0:
            high = mid
        else:
            low = mid
    return (low + high) / 2


n = float(input())
result = solve(n)
print(f"{result:.6f}")
