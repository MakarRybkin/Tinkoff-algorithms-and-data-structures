def count_less_equal(x, n):
    count = 0
    for i in range(1, n + 1):
        count += min(n, x // i)
    return count

def find_kth_number(n, k):
    left, right = 1, n * n
    while left < right:
        mid = (left + right) // 2
        if count_less_equal(mid, n) < k:
            left = mid + 1
        else:
            right = mid
    return left

n, k = map(int, input().split())
result = find_kth_number(n, k)
print(result)
