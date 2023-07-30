import sys
num_cases = int(input())
stack=[]
FLAG=0
for i in range(num_cases):
    cases = str(input())
    ####
    # 구현
    #print(cases)
    stack=[]
    FLAG=0
    for letter in cases:
        # print(letter)
        if letter=='(':
            stack.append(letter)
        elif letter==')':
            try:
                stack.pop()
            except:
                FLAG=1
                print("NO")
                # print("----------------------")
                break
    if FLAG==0:
        # print(stack)
        if len(stack)==0:
            print("YES")
        else:
            print("NO")
        # print("------------------------")
    else:
        pass

    ####
