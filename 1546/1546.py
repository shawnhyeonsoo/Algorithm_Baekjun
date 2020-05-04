N = int(input())
A = list(map(int,input().split()))

M = max(A)
B = []
for t in range(0,N):
    B.append((A[t]/M)*100)
C = sum(B)/N
print(C)