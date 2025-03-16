def time_to_seconds(h, m, s):
    return h * 3600 + m * 60 + s


import sys

N = int(sys.stdin.readline())
events = []

for i in range(1, N + 1):
    h1, m1, s1, h2, m2, s2 = [int(x) for x in sys.stdin.readline().split()]
    open_time = time_to_seconds(h1, m1, s1)
    close_time = time_to_seconds(h2, m2, s2)

    if open_time < close_time:
        events.append((open_time, 'open'))
        events.append((close_time, 'close'))
    else:
        events.append((open_time, 'open'))
        events.append((86400, 'close'))
        events.append((0, 'open'))
        events.append((close_time, 'close'))

events.sort(key=lambda x: (x[0], x[1] == 'close'))

current_open = 0
last_time = 0
total_time = 0

for time, event_type in events:
    if current_open == N:
        total_time += time - last_time

    if event_type == 'open':
        current_open += 1
    else:
        current_open -= 1

    last_time = time

print(total_time)


