N = int(input())
A = []
B = []
count = 0
for i in range(N):
    start,end = map(int,input().split())
    A.append((start,end))

A = sorted(A, key=lambda A: (A[1],A[0]))

for j in range(len(A)):
    if len(B) == 0:
        B.append(A[j])
        count += 1
    elif A[j][0] >= B[-1][1]:
        B.append(A[j])
        count +=1
    else:
        pass

print(count)