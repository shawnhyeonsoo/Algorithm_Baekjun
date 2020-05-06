given = int(input())
i = 0

if given == 1:
    answer = 1

else:

    while True:
        if given < 2+ 6*(i*(i-1))/2 :
            answer = i
            break
        else:
            i += 1

print(answer)