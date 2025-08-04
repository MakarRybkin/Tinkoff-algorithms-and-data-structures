import sys


def solve():
    s = sys.stdin.readline().strip()
    n = len(s)

    # dp[i][j] will store the shortest compressed string for s[i...j]
    dp = [[None] * n for _ in range(n)]

    # Initialize base cases: single characters
    # For a substring of length 1, the compressed form is just the character itself.
    for i in range(n):
        dp[i][i] = s[i]

    # Fill the dp table for increasing lengths of substrings
    # 'length' here refers to the actual length of the substring (j - i + 1)
    for length in range(2, n + 1):
        # 'i' is the starting index of the substring
        for i in range(n - length + 1):
            # 'j' is the ending index of the substring
            j = i + length - 1

            # Option 1: No compression (just the substring itself)
            # This serves as the initial "worst case" length for comparison
            dp[i][j] = s[i: j + 1]

            # Option 2: Concatenation
            # Try all possible split points 'k' within the substring s[i...j]
            # A split at 'k' divides the substring into s[i...k] and s[k+1...j]
            for k in range(i, j):
                combined_str = dp[i][k] + dp[k + 1][j]
                # If concatenating two already compressed parts results in a shorter string, update dp[i][j]
                if len(combined_str) < len(dp[i][j]):
                    dp[i][j] = combined_str

            # Option 3: Repetition
            # Check if the substring s[i...j] can be represented as X(S)
            sub_len = length
            # Iterate through possible periods (lengths of the repeating base unit)
            # A period must be a divisor of sub_len and smaller than sub_len itself.
            for period in range(1, sub_len):
                if sub_len % period == 0:  # Check if 'period' is a valid divisor

                    # Assume it's repeating until proven otherwise
                    is_repeating = True
                    # The base unit for repetition is the prefix of length 'period'

                    # Compare each part of the substring with the assumed base unit
                    # We check if s[i+char_idx] matches s[i + (char_idx % period)] for all characters
                    for char_idx_offset in range(period, sub_len):
                        if s[i + char_idx_offset] != s[i + (char_idx_offset % period)]:
                            is_repeating = False
                            break

                    if is_repeating:
                        count = sub_len // period  # Number of times the base unit repeats

                        # Get the already computed compressed form of the base unit
                        compressed_base_unit = dp[i][i + period - 1]

                        # Form the current candidate compressed string for repetition
                        current_compressed_str = str(count) + "(" + compressed_base_unit + ")"

                        # If this repetition form is shorter, update dp[i][j]
                        if len(current_compressed_str) < len(dp[i][j]):
                            dp[i][j] = current_compressed_str

    # The final answer is the shortest compressed string for the entire input string s[0...n-1]
    sys.stdout.write(dp[0][n - 1] + "\n")


solve()