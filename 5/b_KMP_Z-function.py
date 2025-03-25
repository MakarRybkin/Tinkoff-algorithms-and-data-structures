# Можно реализовать красивее, но это самое straightforward O(n) написание по алгоритму
# красивую реализацию можно подсмотреть тут https://neerc.ifmo.ru/wiki/index.php?title=Z-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D1%8F
def zFunction(S):
    result = len(S) * [0]
    l = -1
    r = -1
    for i in range(1, len(S)):
        if i > r:
            x = 0
            while x + i < len(S) and S[x] == S[x + i]:
                x += 1
            result[i] = x
            if x + i - 1 > r:
                l = i
                r = x + i - 1
        else:
            if result[i - l] + i <= r:
                result[i] = result[i - l]
            else:
                x = min(result[i - l], r - i) # не выйдет просто поставить result[i - l], т.к. он далековат
                while x + i < len(S) and S[x + i] == S[x]:
                    x += 1
                l = i
                r = i + x - 1
                result[i] = x
    return result
# print(zFunction('abacababacababa'))
# print(zFunction('ababa'))

def findAllOccurencesWithoutHash(S, T):
    concat = T + '$' + S
    zf = zFunction(concat)
    result = []
    for i in range(len(T), len(concat)):
        if zf[i] == len(T):
            result.append(i - len(T) - 1)
    return result


print(findAllOccurencesWithoutHash('aabzcaabzaabza', 'aabza'))
print(findAllOccurencesWithoutHash('abaacabaaa', 'aba'))