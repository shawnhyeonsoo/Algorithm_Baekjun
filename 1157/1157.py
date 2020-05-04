given = input()
given = given.lower()
given_compare = list(set(given))
A = []
B = []

for i in range(0,len(given_compare)):
    A.append(given.count(given_compare[i]))
    B.append(given.count(given_compare[i]))

A = sorted(A)

if len(A) == 1:
    answer = given

elif A[-1] == A[-2]:
    answer = '?'

else:
    answer = given_compare[B.index(max(A))]

print(answer.upper())