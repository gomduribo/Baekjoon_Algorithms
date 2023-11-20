def solution(s):
    word_dic={"":"","zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    num_list=['0','1','2','3','4','5','6','7','8','9']
    word=''
    result=''
    for c in s:
        # print(f"c:{c} word: {word} result: {result}")
        if(c not in num_list):
            word=word+c
            if word in word_dic.keys():
                result=result+word_dic[word]
                word=''
            continue
        else:
            result=result+c
            word=''
    # print(f"result:{result}")
    return int(result)
