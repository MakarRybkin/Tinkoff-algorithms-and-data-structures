from sys import stdin
def find_max_sub_arr_product(n: int, a: list[int]):
    min_ind = [-1 for _ in range(n)]
    stack_ind = list()
    for i in range(n):
        while len(stack_ind) > 0 and a[i] < a[stack_ind[-1]]:
            stack_ind.pop()
        if len(stack_ind) > 0:
            min_ind[i] = stack_ind[-1]
        stack_ind.append(i)

    max_ind = [n for _ in range(n)]
    stack_ind = list()
    for i in range(0, n):
        while len(stack_ind) > 0 and a[n - i - 1] <= a[stack_ind[-1]]:
            stack_ind.pop()
        if len(stack_ind) > 0:
            max_ind[n - i - 1] = stack_ind[-1]
        stack_ind.append(n - i - 1)

    prefix_sum = list([0])
    for i in range(n):
        prefix_sum.append(prefix_sum[i] + a[i])

    ans = 0
    for i in range(n):
        sub_arr_sum = prefix_sum[max_ind[i]] - prefix_sum[min_ind[i]+1]
        ans = max(ans, a[i] * sub_arr_sum)
    print(ans)

n = int(stdin.readline())
a = [int(x) for x in stdin.readline().split()]
find_max_sub_arr_product(n, a)