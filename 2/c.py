import sys
input = sys.stdin.readline().split()
stack1 = []
result = 0
def operate (operation):
    if operation == '+':
        a=stack1.pop()
        b=stack1.pop()
        stack1.append(a+b)
    if operation == '-':
        a=stack1.pop()
        b=stack1.pop()
        stack1.append(b-a)
    if operation == '/':
        a=stack1.pop()
        b=stack1.pop()
        stack1.append(b//a)
    if operation == '*':
        a=stack1.pop()
        b=stack1.pop()
        stack1.append(a*b)
for i in input:
    if i.isdigit():
        stack1.append(int(i))
    elif i in ['-','+','*','/']:
        operate(i)
print(*stack1)
