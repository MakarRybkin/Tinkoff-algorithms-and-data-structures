import sys

n = int(sys.stdin.readline().split()[0])
balls = sys.stdin.readline().split()
counter = 1
result = 0
stack =[]
for i in range(n):
    if stack:
        if balls[i] == stack[-1][0]:
            counter += 1
        elif balls[i] != stack[-1][0] :
            if counter >= 3:
                for _ in range(counter):
                    stack.pop()
                    result+=1
                if balls[i] == stack[-1][0]:
                    counter = stack[-1][1] +1
                else:
                    counter = 1
            else:
                counter = 1
    stack.append([balls[i],counter])
if counter >= 3:
    result += counter
print(result)