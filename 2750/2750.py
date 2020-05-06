test = int(input())
A = []
for i in range(0,test):
    A.append(int(input()))
    A.sort()

for k in range(0,len(A)):
    print(A[k])
