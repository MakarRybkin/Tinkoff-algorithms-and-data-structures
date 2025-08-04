def power(base, exp):
    res = 1
    mod = 1000000007
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp //= 2
    return res

def modInverse(n):
    return power(n, 1000000007 - 2)

n, k = map(int, input().split())

mod = 1000000007

fact = [1] * (n + 1)
for i in range(1, n + 1):
    fact[i] = (fact[i - 1] * i) % mod

numerator = fact[n]
denominator_k = fact[k]
denominator_nk = fact[n - k]

inv_denominator_k = modInverse(denominator_k)
inv_denominator_nk = modInverse(denominator_nk)

ans = (numerator * inv_denominator_k) % mod
ans = (ans * inv_denominator_nk) % mod

print(ans)