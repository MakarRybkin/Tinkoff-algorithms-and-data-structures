from sys import stdin
n = int(stdin.readline())
operations = []
stack = []
def push (x):
    if stack:
        stack.append([x,min(x,stack[-1][1])])
    else:
        stack.append([x,x])
result=[]
for i in range(1,n+1):
    line = [int(x) for x in stdin.readline().strip().split()]
    if line[0] == 1:
        push(line[1])
        continue
    if line[0] == 2:
        stack.pop()
        continue
    if line[0] == 3:
        result.append(stack[-1][1])

print(*result, sep='\n')