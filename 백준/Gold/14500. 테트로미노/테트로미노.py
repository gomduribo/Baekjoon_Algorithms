N, M = map(int, input().split(" "))

mat=[]
for _ in range(N):
  mat.append(list(map(int, input().split(" "))))

def find_max(matrix):
  result=0
  sums=[]
  for r in range(N):
    for c in range(M):
      if(c+1<M and r+1<N):#1
        sums.append(matrix[r][c]+matrix[r][c+1]+matrix[r+1][c]+matrix[r+1][c+1])
        
      if(c+3<M):#2-1
        sums.append(matrix[r][c]+matrix[r][c+1]+matrix[r][c+2]+matrix[r][c+3])
      if(r+3<N):#2-2
        sums.append(matrix[r][c]+matrix[r+1][c]+matrix[r+2][c]+matrix[r+3][c])
        
      if(r+2<N and c+1<M):#3-1
        sums.append(matrix[r][c]+matrix[r+1][c]+matrix[r+2][c]+matrix[r+2][c+1])
        sums.append(matrix[r][c]+matrix[r][c+1]+matrix[r+1][c+1]+matrix[r+2][c+1])
        sums.append(matrix[r][c]+matrix[r][c+1]+matrix[r+1][c]+matrix[r+2][c])
        sums.append(matrix[r][c+1]+matrix[r+1][c+1]+matrix[r+2][c+1]+matrix[r+2][c])
      if(r+1<N and c+2<M):#3-2
        sums.append(matrix[r][c]+matrix[r+1][c]+matrix[r+1][c+1]+matrix[r+1][c+2])
        sums.append(matrix[r][c]+matrix[r][c+1]+matrix[r][c+2]+matrix[r+1][c])
        sums.append(matrix[r][c]+matrix[r][c+1]+matrix[r][c+2]+matrix[r+1][c+2])
        sums.append(matrix[r+1][c]+matrix[r+1][c+1]+matrix[r+1][c+2]+matrix[r][c+2])

      if(r+1<N and c+2<M):#4-1
        sums.append(matrix[r][c+1]+matrix[r+1][c]+matrix[r+1][c+1]+matrix[r+1][c+2])
        sums.append(matrix[r][c]+matrix[r][c+1]+matrix[r][c+2]+matrix[r+1][c+1])
      if(r+2<N and c+1<M):#4-2
        sums.append(matrix[r+1][c]+matrix[r][c+1]+matrix[r+1][c+1]+matrix[r+2][c+1])
        sums.append(matrix[r][c]+matrix[r+1][c]+matrix[r+2][c]+matrix[r+1][c+1])

      if(r+1<N and c+2<M):#5-1
        sums.append(matrix[r][c+1]+matrix[r][c+2]+matrix[r+1][c]+matrix[r+1][c+1])
        sums.append(matrix[r][c]+matrix[r][c+1]+matrix[r+1][c+1]+matrix[r+1][c+2])
      if(r+2<N and c+1<M):#5-2
        sums.append(matrix[r][c]+matrix[r+1][c]+matrix[r+1][c+1]+matrix[r+2][c+1])
        sums.append(matrix[r][c+1]+matrix[r+1][c]+matrix[r+1][c+1]+matrix[r+2][c])

  result=max(sums)  
    
        
  return result

ans=find_max(mat)
print(ans)