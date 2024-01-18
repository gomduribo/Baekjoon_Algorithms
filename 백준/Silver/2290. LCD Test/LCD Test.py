line=input().split(" ")
s=int(line[0])
n=line[1]

def make_digit(num,s):
  lcd=[[" "]*(s+2) for _ in range(2*s+3)]
  for i in range(1,s+1):
    if num in '23567890': #a
      lcd[0][i]='-'
    if num in '12347890': #b
      lcd[i][-1]='|'
    if num in '134567890': #c
      lcd[s+1+i][-1]='|'
    if num in '2356890': #d
      lcd[2*s + 2][i]='-'
    if num in '2680': #e
       lcd[s+1+i][0]='|'
    if num in '456890': #f
       lcd[i][0] ='|'
    if num in '2345689': #g
       lcd[s+1][i] ='-'

  return lcd

result=[make_digit(num,s) for num in n]

for line in zip(*result):
  for r in line:
      print(''.join(r), end=' ')
  print()