import sys
from collections import deque
input = sys.stdin.read
data = input().split()

n = int(data[0])
k = int(data[1])
line = list(map(int, data[2:2 + n]))

deque1 = deque()
result = []
for i in range(n):
    deque1.append(line[i])
    if len(deque1)>=k:
        result.append(min(deque1))
        deque1.popleft()
print(*result)

# from collections import deque
# import sys


# def main():
#     input = sys.stdin.read
#     data = input().split()
#
#     N = int(data[0])
#     K = int(data[1])
#     numbers = list(map(int, data[2:2 + N]))
#
#     deq = deque()
#     result = []
#
#     for i in range(N):
#         # Удаляем элементы, которые больше текущего
#         while deq and numbers[i] <= deq[-1][0]:
#             deq.pop()
#
#         # Добавляем текущий элемент и его индекс
#         deq.append((numbers[i], i))
#
#         # Удаляем элементы, которые выходят за пределы окна
#         if deq[0][1] < i - K + 1:
#             deq.popleft()
#
#         # Добавляем результат в список, когда окно заполнено
#         if i >= K - 1:
#             result.append(deq[0][0])
#
#     print(' '.join(map(str, result)))
#
#
# if __name__ == "__main__":
#     main()
