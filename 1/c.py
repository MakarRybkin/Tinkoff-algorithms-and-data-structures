import sys

n = int(input())


def binary_search( low, high) -> int:
    if low <= high:
        mid= (low + high) // 2
        response = query(mid)
        if response == "<":
            return binary_search(low, mid - 1)
        elif response == ">=":
            return binary_search(mid + 1, high)
    return low - 1


def query(x):
    print(x)
    sys.stdout.flush()
    return input()

print(f'! {binary_search(1, n)}')
sys.stdout.flush()