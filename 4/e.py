def can_split(max_sum, k):
    count = 1
    current_sum = 0

    for num in numbers:
        if current_sum + num > max_sum:
            count += 1
            current_sum = num
            if count > k:
                return False
        else:
            current_sum += num

    return True


def binary_search():
    left, right = max(numbers), sum(numbers)
    while left < right:
        mid = (left + right) // 2
        if can_split(mid, k):
            right = mid-1
        else:
            left = mid + 1
    return left


n, k = map(int, input().split())
numbers = list(map(int, input().split()))

print(binary_search())
