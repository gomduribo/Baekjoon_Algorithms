N,M=map(int, input().split(" "))
ans=[]

def Back(start, N,M):
  if len(ans)==M:
    print(" ".join(map(str, ans)))
    return

  for i in range(start,1+N):
    if i not in ans:
      ans.append(i)
      Back(i,N,M)
      ans.pop()

Back(1,N,M)