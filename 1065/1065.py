N = int(input())
count = 0

for k in range(1, N+1):
    hunds = k // 100
    tens = (k - hunds * 100) // 10
    ones = k % 10
    diff1 = hunds - tens
    diff2 = tens - ones
    if k < 100:
        count += 1
    elif diff1 == diff2:
        count +=1

print(count)