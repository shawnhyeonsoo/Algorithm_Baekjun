A, B, C = map(int, input().split())

count = 0

if B < C:
    count = A // (C - B)
    print(count + 1)

else:
    print(-1)