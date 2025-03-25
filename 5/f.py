import sys
def countPalindromicSubstringsWithoutHash(S):
    odd = len(S) * [1] # Надо добавить сразу палиндром из одного символа
    even = (len(S) - 1) * [0] # А тут не надо

    l = 0
    r = 0
    for i in range(1, len(S)): # обработка нечетных палиндромов
        if i < r:
            odd[i] = min(r - i + 1, odd[l + r - i])
        while i - odd[i] >= 0 and i + odd[i] < len(S) and S[i - odd[i]] == S[i + odd[i]]:
            odd[i] += 1
        if i + odd[i] - 1 > r:
            l = i - odd[i] + 1
            r = i + odd[i] - 1
    l = -1
    r = -1
    for i in range(0, len(S) - 1): # обработка четных палиндромов
        if i < r:
            even[i] = min(r - i, even[l + r - i - 1])
        while i - even[i] >= 0 and i + even[i] + 1 < len(S) and S[i - even[i]] == S[i + even[i] + 1]:
            even[i] += 1
        if i + even[i] > r:
            l = i - even[i] + 1
            r = i + even[i]

    result = 0
    for i in range(len(S)):
        result += odd[i]
    for i in range(len(S) - 1):
        result += even[i]
    return result


s= sys.stdin.readline().strip()
print(countPalindromicSubstringsWithoutHash(s))