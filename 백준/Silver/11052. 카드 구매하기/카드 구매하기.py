import sys

inpuy=sys.stdin.readline
N=int(input())
n=1
p_list=list(map(int, input().split(" ")))
p_list.insert(0, 0)
# print(p_list)
results=[0]*(N+1)

while n!=N+1:
  results[n]=p_list[n]
  for i in range(1, n):
    if results[i]+results[n-i]>results[n]:
      results[n]=results[i]+results[n-i]

  n=n+1

print(results[N])