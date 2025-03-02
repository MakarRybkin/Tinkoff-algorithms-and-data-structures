from collections import deque
import sys


data = sys.stdin.read().splitlines()

n = int(data[0])
queue = deque()
index_map = {}
result = []

for i in range(1, n + 1):
    event = [int(x) for x in data[i].split()]
    event_type = event[0]

    if event_type == 1:
        person_id = event[1]
        queue.append(person_id)
        index_map[person_id] = len(queue) - 1

    elif event_type == 2:
        if queue:
            person_id = queue.popleft()
            del index_map[person_id]
            for key in index_map.keys():
                if index_map[key] > 0:
                    index_map[key] -= 1

    elif event_type == 3:
        if queue:
            person_id = queue.pop()
            del index_map[person_id]

    elif event_type == 4:
        q = event[1]
        if q in index_map:
            result.append(index_map[q])
        else:
            result.append(0)

    elif event_type == 5:
        if queue:
            result.append(queue[0])
        else:
            result.append(0)

print('\n'.join(map(str, result)))
