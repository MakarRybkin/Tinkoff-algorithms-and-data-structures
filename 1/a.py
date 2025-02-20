def binary_search(a, b, low, high) -> str:
    if low > high :
        return "NO"
    mid = (low + high) // 2
    if a[mid] > b:
        return binary_search(a, b, low, mid - 1)
    elif a[mid] < b:
        return binary_search(a, b, mid + 1, high)
    elif a[mid] == b:
        return "YES"
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(k):
    print(binary_search(a, b[i], 0, len(a) - 1))
