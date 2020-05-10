min_no = int(input())
max_no = int(input())
B = []

for number in range(min_no,max_no+1):
    count = 0
    for j in range(1,number+1):
        if number%j == 0:
            count += 1
        else:
            pass

    if count == 2:
        B.append(number)
    else:
        pass

if len(B) > 0:
    print(sum(B))
    print(min(B))
else:
    print('-1')