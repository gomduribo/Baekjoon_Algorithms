import sys
from collections import deque

input=sys.stdin.readline

N,K=map(int, input().split(" "))
rail=list(map(int, input().split(" ")))
rail_q=deque(rail)
robot=[0]*N
robots=deque(robot)

cnt=0 # 내구도가 0인 컨베이어 수
process=0

# print(rail)
# print(rail_q)
# rail_q.rotate(-1)
# print(rail_q)
while cnt<K:
  
  #벨트 돌리기
  rail_q.rotate()

  # 내리는 위치에 있는 로봇 떨구기
  robots[N-1]=0
  
  robots.rotate()
  robots[N-1]=0
  

  # 로봇이 이동
  for i in range(N-2,-1,-1):

    if robots[i]==1: #해당칸에 로봇이 있다면
      #앞쪽이 비었고, 내구도가 1이상이라면 이동
      if robots[i+1]==0 and rail_q[i+1]>=1: 
        robots[i+1]=1
        rail_q[i+1]-=1
        robots[i]=0
  
  #올리는곳에 로봇이 없고,내구도가 1이상이라면 로봇 올리기
  if rail_q[0]>=1 and robots[0]!=1:  
    robots[0]=1
    rail_q[0]=rail_q[0]-1

  cnt=rail_q.count(0)
  process+=1
  # print("-----")
  # print(f"{rail_q}")
  # print(f"{robots}")

print(process)
