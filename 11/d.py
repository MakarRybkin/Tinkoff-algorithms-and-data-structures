import sys


def solve():
    L, N = map(int, sys.stdin.readline().split())
    C = list(map(int, sys.stdin.readline().split()))

    # Add 0 and L to the cut positions
    all_cuts = [0] + C + [L]
    all_cuts.sort()  # Ensure sorted, though problem states C is strictly increasing

    num_points = len(all_cuts)

    # dp[i][j] will store the minimum cost to cut the segment from all_cuts[i] to all_cuts[j]
    dp = [[0] * num_points for _ in range(num_points)]

    # Iterate over the length of the segments (diff in indices)
    # length = 1 means segment of 2 points, 0 cuts needed (base case, cost 0)
    # length = 2 means segment of 3 points, 1 cut needed (e.g., all_cuts[i] to all_cuts[i+2], cut at all_cuts[i+1])
    for length in range(2, num_points):
        for i in range(num_points - length):
            j = i + length

            # The cost of cutting this segment (all_cuts[j] - all_cuts[i])
            # is added regardless of where the first cut is made.
            # We then add the costs of the two subproblems.
            current_segment_cost = all_cuts[j] - all_cuts[i]

            min_cost_for_segment = float('inf')

            # Try all possible intermediate cut points k
            # k is the index of the cut point in all_cuts
            # k must be between i and j (exclusive)
            for k in range(i + 1, j):
                cost = current_segment_cost + dp[i][k] + dp[k][j]
                min_cost_for_segment = min(min_cost_for_segment, cost)

            dp[i][j] = min_cost_for_segment

    sys.stdout.write(str(dp[0][num_points - 1]) + "\n")


solve()