def prime_factorization(n):
    factors = {}
    d = 2
    temp = n

    while temp % d == 0:
        factors[d] = factors.get(d, 0) + 1
        temp //= d
    d = 3

    while d * d <= temp:
        while temp % d == 0:
            factors[d] = factors.get(d, 0) + 1
            temp //= d
        d += 2

    if temp > 1:
        factors[temp] = factors.get(temp, 0) + 1

    result_parts = []
    for prime_factor in sorted(factors.keys()):
        count = factors[prime_factor]
        if count == 1:
            result_parts.append(str(prime_factor))
        else:
            result_parts.append(f"{prime_factor}^{count}")

    return "*".join(result_parts)


N = int(input())

print(prime_factorization(N))