def min_lex_cyclic_shift(S):
    S = S + S
    n = len(S) // 2
    f = [-1] * (2 * n)
    k = 0

    for j in range(1, 2 * n):
        i = f[j - k - 1]
        while i != -1 and S[j] != S[k + i + 1]:
            if S[j] < S[k + i + 1]:
                k = j - i - 1
            i = f[i]

        if S[j] != S[k + i + 1]:
            if S[j] < S[k]:
                k = j
            f[j - k] = -1
        else:
            f[j - k] = i + 1

    return S[k:k + n]


S = input().strip()
print(min_lex_cyclic_shift(S))