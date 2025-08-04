MOD = 10**9 + 9

def generate_valid_triples():
    is_prime = [False] * 1000
    for i in range(100, 1000):
        prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            is_prime[i] = True
    valid = []
    for i in range(100, 1000):
        if is_prime[i]:
            digits = [int(d) for d in str(i)]
            valid.append(tuple(digits))
    return valid

def count_passwords(n):
    valid_triples = generate_valid_triples()

    from collections import defaultdict
    transitions = defaultdict(list)
    for a, b, c in valid_triples:
        transitions[(a, b)].append(c)

    dp = [[0] * 10 for _ in range(10)]
    for a, b, c in valid_triples:
        dp[b][c] += 1

    for _ in range(4, n + 1):
        new_dp = [[0] * 10 for _ in range(10)]
        for a in range(10):
            for b in range(10):
                count = dp[a][b]
                if count:
                    for c in transitions.get((a, b), []):
                        new_dp[b][c] = (new_dp[b][c] + count) % MOD
        dp = new_dp

    return sum(dp[a][b] for a in range(10) for b in range(10)) % MOD

n = int(input())
print(count_passwords(n))
