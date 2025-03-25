#
# #
n=int(input())
a=list(map(int,input().split()))
# # counter=0
# # for iteration in range(n):
# #     had_swaps = False
# #     counter+=1
# #     for i in range(n - 1):
# #         if a[i] > a[i + 1]:
# #             a[i], a[i + 1] = a[i + 1], a[i]
# #             had_swaps = True
# #     if not had_swaps:
# #         break
# # print(a,counter)


arr = [0] * n
result = [1]
r = 1
pointer = n - 1
for j in range(n - 1):
    arr[a[j] - 1] += 1
    r += 1
    while arr[pointer] == 1:
        pointer -= 1
        r -= 1
    result.append(r)
result.append(1)
print(*result)