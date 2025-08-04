import sys


def last_nonzero_digit_factorial(n):
    if n == 0:
        return 1

    if n < 5:
        if n == 1: return 1
        if n == 2: return 2
        if n == 3: return 6
        if n == 4: return 4

    num_twos = 0
    num_fives = 0
    res = 1

    for i in range(1, n + 1):
        current_num = i

        while current_num % 2 == 0:
            num_twos += 1
            current_num //= 2

        while current_num % 5 == 0:
            num_fives += 1
            current_num //= 5

        res = (res * current_num) % 10

    remaining_twos = num_twos - num_fives

    if remaining_twos > 0:
        remainder_cycle = remaining_twos % 4
        if remainder_cycle == 1:
            res = (res * 2) % 10
        elif remainder_cycle == 2:
            res = (res * 4) % 10
        elif remainder_cycle == 3:
            res = (res * 8) % 10
        elif remainder_cycle == 0:
            res = (res * 6) % 10

    return res


N = int(sys.stdin.readline())
sys.stdout.write(str(last_nonzero_digit_factorial(N)) + '\n')