def power(base, exp, modulus):
    res = 1
    base %= modulus
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % modulus
        base = (base * base) % modulus
        exp //= 2
    return res

N, M, K, MOD = map(int, input().split())

term1 = power(M, N, MOD)
term2 = power(K, MOD - 2, MOD)

ans = (term1 * term2) % MOD

print(ans)