test_case = int(input())
numbers = input().split()
A = []
count = 0
answer = 0
for i in range(0,test_case):
    A.append(int(numbers[i]))
    count = 0
    for j in range(1,A[i]+1):
        if A[i]%j == 0:
            count += 1
        else:
            pass
    if count == 2:
        answer += 1
    else:
        pass

print(answer)