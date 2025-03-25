import sys


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def insert(array, newNum):
    array.append(newNum)
    size = len(array)
    for i in range((size // 2) - 1, -1, -1):
        heapify(array, size, i)


def deleteNode(array, num):
    size = len(array)
    if size == 0:
        return

    try:
        index = array.index(num)
    except ValueError:
        return
    array[index], array[size - 1] = array[size - 1], array[index]
    array.pop()

    heapify(array, len(array), index)


arr = []
n = int(sys.stdin.readline())
for _ in range(n):
    command = [int(x) for x in sys.stdin.readline().split()]
    if command[0] == 0:
        insert(arr, command[1])
    elif command[0] == 1:
        if arr:
            print(arr[0])
            deleteNode(arr, arr[0])
