# def partition(nums, low, high):
#     pivot = nums[(low + high) // 2]
#     i = low - 1
#     j = high + 1
#     while True:
#         i += 1
#         while nums[i] < pivot:
#             i += 1
#
#         j -= 1
#         while nums[j] > pivot:
#             j -= 1
#
#         if i >= j:
#             return j
#         nums[i], nums[j] = nums[j], nums[i]
#
#
# def quick_sort(items, low, high):
#     if low < high:
#         split_index = partition(items, low, high)
#         quick_sort(items, low, split_index)
#         quick_sort(items, split_index + 1, high)
#
# random_list_of_nums = [1,3,2]
# quick_sort(random_list_of_nums, 0, len(random_list_of_nums) - 1)
# print(random_list_of_nums)

n=int(input())

# def worst_case(n):
#     a = [i + 1 for i in range(n)]
#
#     mid = (len(a) - 1) // 2
#     last = a[-1]
#     a.insert(mid, last)
#     a.pop(a[-1])
#     [print(i, end=' ') for i in a]
#
# worst_case(n)

def worst_case(n):
    a = list(range(1, n + 1))

    for i in range(2, len(a)):
        a[i], a[i // 2] = a[i // 2], a[i]

    [print(i, end=' ') for i in a]
worst_case(n)