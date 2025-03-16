from sys import stdin


def count_length_scanlines(scanlines):
    scanlines.sort()

    painted_part = 0
    current_start, current_end = scanlines[0]

    for start, end in scanlines[1:]:
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            painted_part += current_end - current_start
            current_start, current_end = start, end

    painted_part += current_end - current_start

    return painted_part


scanlines = []
n = int(stdin.readline())
for i in range(n):
    scanline = [int(x) for x in stdin.readline().split()]
    scanlines.append(scanline)

print(count_length_scanlines(scanlines))
