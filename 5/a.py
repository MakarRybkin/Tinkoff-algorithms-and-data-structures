from sys import stdin, stdout

MOD = 10 ** 9 + 7
K = 31


def compute_hashes_and_powers(s):
    n = len(s)
    hashes = [0] * (n + 1)
    powers = [1] * (n + 1)

    for i in range(1, n + 1):
        hashes[i] = (hashes[i - 1] * K + (ord(s[i - 1]) - ord('a') + 1)) % MOD
        powers[i] = (powers[i - 1] * K) % MOD

    return hashes, powers


def substring_hash(hashes, powers, l, r):
    return ((hashes[r] - hashes[l - 1] * powers[r - l + 1])% MOD + MOD) % MOD


s = stdin.readline().strip()
m = int(stdin.readline())
hashes, powers = compute_hashes_and_powers(s)

results = []
for _ in range(m):
    a, b, c, d = map(int, stdin.readline().split())
    hash1 = substring_hash(hashes, powers, a, b)
    hash2 = substring_hash(hashes, powers, c, d)
    results.append("Yes" if hash1 == hash2 else "No")

stdout.write("\n".join(results) + "\n")
