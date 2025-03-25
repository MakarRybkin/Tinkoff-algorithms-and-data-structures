def prime_power(n):
    """Вычисляет степени PRIME по модулю MOD."""
    pow = [1] * (n + 1)
    for i in range(1, n + 1):
        pow[i] = (pow[i - 1] * PRIME) % MOD
    return pow

def hash_func(s):
    """Вычисляет префиксные хэши строки."""
    hashes = [0] * (len(s) + 1)
    for i in range(len(s)):
        hashes[i + 1] = (hashes[i] * PRIME + (ord(s[i]) - ord('a') + 1)) % MOD
    return hashes

def get_hash(hashes, power, l, r):
    """Получает хэш подстроки s[l:r] за O(1)."""
    return (hashes[r] - hashes[l] * power[r - l]) % MOD

def cyclic_shifts(s):
    """Находит хэши всех циклических сдвигов строки s."""
    n = len(s)
    shifts = set()
    for i in range(n):
        shift_hash = get_hash(hash_b, power_b, i, i + n)
        shifts.add(shift_hash)
    return shifts

def solve(s1, s2):
    """Считает количество вхождений циклических сдвигов s2 в s1."""
    n1, n2 = len(s1), len(s2)
    count = 0
    for i in range(n1 - n2 + 1):
        substr_h = get_hash(hash_a, power_a, i, i + n2)
        if substr_h in c:
            count += 1
    return count

# Константы
PRIME = 31
MOD = 10**9 + 7

# Ввод данных
a = input().strip()
b = input().strip()

# Префиксные хэши и степени
hash_a = hash_func(a)
hash_b = hash_func(b + b)  # Двойная строка для учета циклических сдвигов
power_a = prime_power(len(a))
power_b = prime_power(len(b) * 2)

# Поиск всех циклических сдвигов b
c = cyclic_shifts(b)

# Вычисляем результат
print(solve(a, b))
