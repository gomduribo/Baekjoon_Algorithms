# n,m=map(int, input().split(" "))

# matrix=[]
# for _ in range(n):
#   matrix.append(list(map(int, input().split(" "))))

# def traverse_n_cal(mat,row,col):
#   global result
#   h=len(mat)
#   w=len(mat[0])
#   dx=[1,-1,0,0]
#   dy=[0,0,1,-1]
#   for i in range(4):
#     nx=col+dx[i]
#     ny=row+dy[i]
#     if nx<0 or nx>=h or ny<0 or ny>=w:
#       result+=mat[row][col]
#       continue

#     if mat[ny][nx]>=mat[row][col]:
#       result+=0
#     elif mat[ny][nx]<mat[row][col]:
#       result+=(mat[row][col]-mat[ny][nx])




# result=0
# for row in range(n):
#   for col in range(m):
#     traverse_n_cal(matrix, row, col)

# result+=(2*n*m)
# print(result)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

up = N * M

left = 0
for i in range(N):
    for j in range(M):
        if j == 0:
            left += arr[i][j]
        else:
            if arr[i][j-1] < arr[i][j]:
                left += arr[i][j] - arr[i][j-1]

front = 0
for j in range(M):
    for i in range(N):
        if i == 0:
            front += arr[i][j]
        else:
            if arr[i-1][j] < arr[i][j]:
                front += arr[i][j] - arr[i-1][j]

answer = 2 * (up + left + front)
print(answer)