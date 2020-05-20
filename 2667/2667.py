def DFS(matrix, cnt, x, y):
    global N
    matrix[x][y]=0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        xpos = x + dx[i]
        ypos = y + dy[i]
        if xpos >= 0 and xpos < N and ypos >= 0 and ypos < N:
            if matrix[xpos][ypos] == 1:
                cnt = DFS(matrix, cnt+1, xpos, ypos)
    return cnt


N = int(input())

A = [list(map(int, input())) for i in range(N)]

ans = []
for i in range(N):
    for j in range(N):
        if A[i][j] == 1:
            ans.append(DFS(A, 1, i, j))

print(len(ans))
for i in sorted(ans):
    print(i)