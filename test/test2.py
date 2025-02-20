n, k = list(map(int, input().split()))
numbers = list(map(int, input().split()))
sorted_numbers = sorted(numbers)

if k == 0:
    if sorted_numbers[0] > 1:
        print(1)
    else:
        print(-1)
elif k == n:
    print(sorted_numbers[-1])
elif sorted_numbers[k - 1] != sorted_numbers[k]:
    print(sorted_numbers[k - 1])
else:
    print(-1)