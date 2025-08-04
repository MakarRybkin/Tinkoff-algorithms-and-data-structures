import sys


def longest_palindromic_subsequence(s: str):
    n = len(s)

    if n == 0:
        return 0, ""

    # dp[i][j] stores the length of the longest palindromic subsequence of s[i...j]
    dp = [[0] * n for _ in range(n)]

    # Base case: A single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1

    # Fill the DP table for substrings of increasing length
    # 'length' represents the length of the current substring (from 2 to n)
    for length in range(2, n + 1):
        # 'i' is the starting index of the substring
        for i in range(n - length + 1):
            # 'j' is the ending index of the substring
            j = i + length - 1

            # If the characters at the ends of the current substring match
            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                # If the characters don't match, take the maximum of the two subproblems
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # Reconstruct the longest palindromic subsequence string
    result_front = []  # Stores the first half of the palindrome characters
    result_back = []  # Stores the second half of the palindrome characters (will be reversed later)

    i, j = 0, n - 1  # Start from the full string

    while i <= j:
        if s[i] == s[j]:
            if i == j:  # Middle character for an odd-length palindrome
                result_front.append(s[i])
            else:  # Characters match and it's not the middle (or palindrome is even length)
                result_front.append(s[i])
                result_back.append(s[j])
            i += 1
            j -= 1
        else:
            # Characters don't match. Move to the subproblem that gave the maximum length.
            # If dp[i+1][j] is greater, exclude s[i]. Otherwise, exclude s[j].
            if dp[i + 1][j] > dp[i][j - 1]:
                i += 1
            else:  # If dp[i+1][j] <= dp[i][j-1], prioritize moving j back (excluding s[j])
                j -= 1

    # Combine the front and reversed back parts to form the full palindrome string
    full_palindrome = "".join(result_front) + "".join(result_back[::-1])

    return dp[0][n - 1], full_palindrome


input_string = sys.stdin.readline().strip()

length, palindrome = longest_palindromic_subsequence(input_string)

sys.stdout.write(str(length) + "\n")
sys.stdout.write(palindrome + "\n")