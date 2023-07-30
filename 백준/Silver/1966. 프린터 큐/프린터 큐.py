import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    num_doc,doc_to_know=map(int,input().split(" "))
    imp_list=list(map(int,input().split(" ")))
    doc_impt=imp_list[doc_to_know]
    imp_seq_list=[]
    for i in range(num_doc):
        imp_seq_list.append((i,imp_list[i]))
    print_doc=''
    cnt=0
    t=imp_seq_list[doc_to_know]
    while print_doc!=t:
        if imp_seq_list[0][1] < max(imp_list):
            imp_seq_list.append(imp_seq_list.pop(0))
            imp_list.append(imp_list.pop(0))
        else:
            # print('--3')
            print_doc=imp_seq_list.pop(0)
            imp_list.pop(0)
            cnt=cnt+1
    
    print(cnt)