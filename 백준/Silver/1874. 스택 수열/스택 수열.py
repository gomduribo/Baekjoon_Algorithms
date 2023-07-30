num_n = int(input())
main_stack=[]
src=1
result=[]
FLAG=1
for i in range(num_n):
    seq_num=int(input())
    while src<=seq_num:
        main_stack.append(src)
        src=src+1
        result.append("+")
    if seq_num==main_stack.pop():
        result.append("-")
    else:
        print("NO")
        FLAG=0
        break
if FLAG:
    for i in range(len(result)):
        print(result[i])