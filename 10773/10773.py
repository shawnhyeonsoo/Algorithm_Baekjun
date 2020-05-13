count = int(input())
stack = []
for i in range(0,count):
    N = int(input())
    if N == 0:
        del stack[-1]
    else:
        stack.append(N)

if not stack:
    print(0)
else:
    print(sum(stack))