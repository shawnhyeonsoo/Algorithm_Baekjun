count = int(input())
A = list(map(int, input().split()))
first = 0
final = 0

while len(A) != 0:
    first += min(A)
    final += first
    A.remove(min(A))

print(final)