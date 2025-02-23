def get_palindrome(arr):
    freq_map = {}
    for char in arr:
        freq_map[char] = freq_map.get(char, 0) + 1

    half = []
    odd_char = ''

    for char in range(ord('A'), ord('Z') + 1):
        char = chr(char)
        if char in freq_map:
            half.extend([char] * (freq_map[char] // 2))
            if odd_char == '' and freq_map[char] % 2 == 1:
                odd_char = char

    first_half = ''.join(half)

    palindrome = first_half
    if odd_char:
        palindrome += odd_char
    palindrome += first_half[::-1]

    return palindrome



n = int(input())
str_input = input().strip()
print(get_palindrome(str_input))
