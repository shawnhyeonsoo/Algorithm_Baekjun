def binary_search(array,value,start,end):
    if start > end:
        print('0')
    else:
        pos = (start + end)//2
        if value > array[pos]:
            binary_search(array,value,pos+1,end)
        elif value < array[pos]:
            binary_search(array,value,start,pos-1)
        elif value == array[pos]:
            print('1')

N = int(input())
A = sorted(list(map(int,input().split())))
M = int(input())
B = list(map(int,input().split()))

for i in range(M):
    binary_search(A,B[i],0,N-1)