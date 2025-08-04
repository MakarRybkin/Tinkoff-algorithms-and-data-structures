
n = int(input())
a = list(map(int, input().split()))

stack = []
max_area = 0

a_extended = a + [0]

for i in range(len(a_extended)):
    current_height = a_extended[i]

    while stack and current_height < a_extended[stack[-1]]:
        h_idx = stack.pop()
        height = a_extended[h_idx]

        if not stack:
            width = i
        else:
            width = i - stack[-1] - 1

        max_area = max(max_area, height * width)

    stack.append(i)

print(max_area)
