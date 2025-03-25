import sys


def find_approximate_matches_kmp(p, t):
    len_p, len_t = len(p), len(t)
    positions = []

    for start in range(len_t - len_p + 1):
        mismatch_count = 0
        j = 0

        for i in range(len_p):
            if p[i] != t[start + i]:
                mismatch_count += 1
                if mismatch_count > 1:
                    break

        if mismatch_count <= 1:
            positions.append(start + 1)

    print(len(positions))
    print(" ".join(map(str, positions)))


p = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

find_approximate_matches_kmp(p, t)
