count = int(input())
a = list(map(int,input().split()))

def merge_and_count(a, left_half, right_half):
    merged_array = []
    i = j = 0
    inv_count = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            merged_array.append(left_half[i])
            i += 1
        else:
            inv_count += len(left_half) - i
            merged_array.append(right_half[j])
            j += 1

    merged_array.extend(left_half[i:])
    merged_array.extend(right_half[j:])

    return merged_array, inv_count


def merge_sort_and_count(a):
    if len(a) <= 1:
        return a, 0

    mid = len(a) // 2
    left_half, left_inv = merge_sort_and_count(a[:mid])
    right_half, right_inv = merge_sort_and_count(a[mid:])

    merged_array, merge_inv = merge_and_count(a, left_half, right_half)

    total_inv = left_inv + right_inv + merge_inv
    return merged_array, total_inv

sorted_a, inversion_count = merge_sort_and_count(a)
print(inversion_count)
[print(i ,end=' ') for i in sorted_a]



