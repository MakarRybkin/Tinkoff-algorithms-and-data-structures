from sys import stdin, stdout
import random

def hashSumStr(S):
    global num_to_hash
    hashS = [0]
    for i in range(len(S)):
        hashS.append(hashS[-1]+num_to_hash[S[i]])
    return hashS


def hashSumSubstr(hashS, l, r):
    return hashS[r+1] - hashS[l]

def isAnagramWithHash(a,b,hashSSUMB,hashSSUMa):
    for i in range(len(b)-1,-1,-1):
        for j in range(i,len(a)):
            for k in range(i,len(b)):
                if hashSumSubstr(hashSSUMa,j-i,j) == hashSumSubstr(hashSSUMB,k-i,k):
                    return i+1
    return 0


n=int(stdin.readline())
a = list(map(int, stdin.readline().split()))
m=int(stdin.readline())
b = list(map(int, stdin.readline().split()))
num_to_hash = {}
for c in a:
    num_to_hash[c] = random.randint(1, 1 << 32)
for c in b:
    if c not in num_to_hash.keys():
        num_to_hash[c] = random.randint(1, 1 << 32)

hashSSUMa = hashSumStr(a)
hashSSUMB = hashSumStr(b)
print(isAnagramWithHash(a,b,hashSSUMB,hashSSUMa))







