def move(n,start,end):
    mid = 6 - start - end
    if n <= 1:
        print(start, end)
        return
    else:
        move(n-1,start,mid)
        move(1,start,end)
        move(n-1,mid,end)

N = int(input())
print((2**N)-1)
move(N,1,3)