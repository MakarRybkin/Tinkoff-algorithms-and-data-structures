n=int(input())
a=list(map(int,input().split()))
for iteration in range(n):
    had_swaps = False
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            had_swaps = True
    if not had_swaps:
        break
print(a)