import sys

# def solve():
#     n = int(sys.stdin.readline().strip()[0])
#     a = [int(x) for x in sys.stdin.readline().strip().split()]
#     result = []
#     stack = []
#     x = 1
#     counter= 0
#
#     i = 0
#     while i < n:
#         stack.append(a[i])
#         counter += 1
#         i += 1
#
#         while i < n and a[i] < stack[-1]:
#             stack.append(a[i])
#             counter += 1
#             i += 1
#
#         if x != stack[-1]:
#             print(0)
#             return
#
#         result.append((1, counter))
#         counter = 0
#
#         while stack and x == stack[-1]:
#             counter += 1
#             x += 1
#             stack.pop()
#
#         result.append((2, counter))
#         counter = 0
#
#     if stack:
#         print(0)
#         return
#
#     print(len(result))
#     for action in result:
#         print(action[0], action[1])
# solve()
import sys


def solve():
    # Read the number of elements
    n = int(sys.stdin.readline().strip())
    # Read the list of integers
    a = [int(x) for x in sys.stdin.readline().strip().split()]

    result = []
    stack = []
    x = 1
    counter = 0

    i = 0
    while i < n:
        stack.append(a[i])
        counter += 1
        i += 1

        # Process elements while they are less than the top of the stack
        while i < n and a[i] < stack[-1]:
            stack.append(a[i])
            counter += 1
            i += 1

        # Ensure the top of the stack matches the expected sequence
        if x != stack[-1]:
            print(0)
            return

        result.append((1, counter))  # Action 1
        counter = 0

        # Pop elements from the stack while they match the expected value
        while stack and x == stack[-1]:
            counter += 1
            x += 1
            stack.pop()

        result.append((2, counter))  # Action 2
        counter = 0

    # Check if the stack is empty at the end
    if stack:
        print(0)
        return

    # Print the results
    print(len(result))
    for action in result:
        print(action[0], action[1])


# Call the solve function
solve()
