import sys

# Global variables to store the best solution found
min_coins_count = float('inf')
best_combination = []


# N: target sum
# M: number of coin types
# A: list of coin denominations
# current_index: the index of the coin denomination currently being considered
# current_sum: the sum accumulated so far
# current_coins_used: the number of coins used so far in the current path
# path: a list to store the denominations of coins used in the current path
def find_solution(N, M, A, current_index, current_sum, current_coins_used, path):
    global min_coins_count
    global best_combination

    # Pruning 1: If the current sum already exceeds N, this path is invalid.
    if current_sum > N:
        return

    # Pruning 2: If we've already used more coins than the best solution found so far,
    # this path cannot be better.
    if current_coins_used >= min_coins_count:
        return

    # Base case: All coin denominations have been considered
    if current_index == M:
        if current_sum == N:
            # We found a solution that exactly matches N!
            if current_coins_used < min_coins_count:
                min_coins_count = current_coins_used
                best_combination = path[:]  # Make a copy of the current path
        return

    # Recursive steps: For each coin denomination A[current_index], we have 3 options:

    # Option 1: Use 0 coins of denomination A[current_index]
    find_solution(N, M, A, current_index + 1, current_sum, current_coins_used, path)

    # Option 2: Use 1 coin of denomination A[current_index]
    # Only proceed if adding this coin doesn't exceed N
    if current_sum + A[current_index] <= N:
        path.append(A[current_index])  # Add the coin to the current path
        find_solution(N, M, A, current_index + 1, current_sum + A[current_index], current_coins_used + 1, path)
        path.pop()  # Backtrack: remove the coin to explore other options

    # Option 3: Use 2 coins of denomination A[current_index]
    # Only proceed if adding these two coins doesn't exceed N
    if current_sum + 2 * A[current_index] <= N:
        path.append(A[current_index])  # Add the first coin
        path.append(A[current_index])  # Add the second coin
        find_solution(N, M, A, current_index + 1, current_sum + 2 * A[current_index], current_coins_used + 2, path)
        path.pop()  # Backtrack
        path.pop()  # Backtrack


def main():
    global min_coins_count
    global best_combination

    # Read N and M from the first line
    first_line = sys.stdin.readline().split()
    N = int(first_line[0])
    M = int(first_line[1])

    # Read coin denominations from the second line
    A = list(map(int, sys.stdin.readline().split()))

    # Calculate the total money available from all coins
    total_money_available = sum(2 * a for a in A)

    # Case: Not enough money in total to reach N
    if total_money_available < N:
        sys.stdout.write("-1\n")
        return

    # Start the recursive search
    # We begin from the first coin denomination (index 0), with a sum of 0,
    # 0 coins used, and an empty list for the current path.
    find_solution(N, M, A, 0, 0, 0, [])

    # Output the result based on the search outcome
    if min_coins_count == float('inf'):
        # If min_coins_count is still infinity, it means no exact solution was found
        sys.stdout.write("0\n")
    else:
        # A solution was found! Output the count and the denominations.
        sys.stdout.write(str(min_coins_count) + "\n")
        # Sorting the coins for consistent output, as per problem statement, any order is fine.
        best_combination.sort()
        sys.stdout.write(" ".join(map(str, best_combination)) + "\n")


if __name__ == "__main__":
    main()