N = int(input())
aggregate = 0
count = 0
while aggregate < N:
    count += 1
    aggregate += count


if count%2 == 0: #even
    num = count - aggregate + N
    den = count - num + 1

else:
    num = 1+aggregate-N
    den = count - num + 1

print("{}/{}".format(num,den))