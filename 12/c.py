import sys

MAX_N = 10**6
is_prime = [True] * (MAX_N + 1)
is_prime[0] = is_prime[1] = False

for p in range(2, int(MAX_N**0.5) + 1):
    if is_prime[p]:
        for multiple in range(p * p, MAX_N + 1, p):
            is_prime[multiple] = False

n = int(sys.stdin.readline())

for p in range(2, n // 2 + 1):
    if is_prime[p]:
        q = n - p
        if is_prime[q]:
            sys.stdout.write(f"{p} {q}\n")
            break