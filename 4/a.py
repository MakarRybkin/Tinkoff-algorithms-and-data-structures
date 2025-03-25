import sys
sys.setrecursionlimit(10000)
data=sys.stdin.readlines()
numbers=[int(x) for x in data[1].split()]
b=int(data[2])

result_sum=[0]
result_Xor=[0]

for i in range(len(numbers)):
    result_sum.append(result_sum[i]+numbers[i])

for i in range(len(numbers)):
    result_Xor.append(result_Xor[i]^numbers[i])

for i in range(b):
    line=([int(x) for x  in data[3+i].split()])
    if line[0]==2:
        print(result_Xor[line[1]-1]^result_Xor[line[2]])
    if line[0]==1:
        print(result_sum[line[2]]-result_sum[line[1]-1])
