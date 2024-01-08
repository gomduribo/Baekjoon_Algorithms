first_line=list(map(int, input().split(" ")))
n=first_line[0]
l=first_line[1]
pipe=list(map(int, input().split(" ")))
pipe.sort()
start=pipe[0]
count=1

for i in pipe[1:]:
    if(i+0.5<=start-0.5+l):
        continue
    else:
        start=i
        count+=1
print(count)