import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
q = int(input())

for _ in range(q):
    query = list(map(int, input().split()))

    if query[0] == 1:  # Запрос суммы
        l, r = query[1] - 1, query[2] - 1
        print(sum(arr[l:r + 1]))

    else:  # XOR обновление
        l, r, x = query[1] - 1, query[2] - 1, query[3]
        for i in range(l, r + 1):
            arr[i] ^= x