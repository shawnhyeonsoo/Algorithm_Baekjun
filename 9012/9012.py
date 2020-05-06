count = int(input())
for i in range(count):
    A = list(input())
    stack = 0
    for j in range(len(A)):
        if A[j] == '(':
            stack += 1
        else:
            stack -= 1
        if stack < 0:
            print('NO')
            break

    if stack == 0:
        print('YES')
    elif stack >0:
        print('NO')
