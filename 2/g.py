
from collections import deque
from sys import stdin


def main():
    n = int(stdin.readline().split()[0])

    first_part = deque()
    second_part = deque()
    k1 = 0
    k2 = 0

    for _ in range(n):
        t = stdin.readline().split()

        if t[0] == '-':
            val = first_part.popleft()
            print(val)
            k1 -= 1
        elif t[0] == '+':
            second_part.append(t[-1])
            k2 += 1
        else:
            second_part.appendleft(t[-1])
            k2 += 1

        if k1 < k2:
            first_part.append(second_part.popleft())
            k2 -= 1
            k1 += 1


if __name__ == "__main__":
    main()

