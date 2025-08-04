import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    gcd_val = gcd(a, b)
    return (a // gcd_val) * b

line = sys.stdin.readline().split()
N = int(line[0])
K = int(line[1])

result = lcm(N, K)
sys.stdout.write(str(result) + '\n')