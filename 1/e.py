a,b,c,d = map(int,input().split())
def f(x):
    return a*x**3 + b*x**2 + c*x + d
def binary_search():
    eps = 1e-10
    low, high = -10**6,10**6
    while high - low > eps:
        mid = (low + high) / 2
        if f(low) * f(mid) <= 0:
            high = mid
        else:
            low = mid
    return (low + high) / 2

result = binary_search()
print(f"{result:.10f}")