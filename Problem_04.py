"""
第 0004 题： 任一个英文的纯文本文件，统计其中的单词出现的个数。
"""

import re

def get_word_frequencies(file_name):
    dic = {}
    txt = open(file_name, 'r').read().splitlines()

    n=0
    for line in txt:
        print(line)
        line = re.sub(r'[.?!,""/]', ' ', line)   #要替换的标点符号，英文字符可能出现的
        line = re.sub(r' - ', ' ', line) #替换单独的‘-’ 
        for word in line.split():
            if word[-1] =='-':#当一行的最后一个字符是-的时候，需要跟下一个英文字符串联起来构成单词
                    m=word[:-1]
                    n=1
                    break
            if n==1:
                word=m+word
                n=0
            print(word) 
            dic.setdefault(word.lower(), 0)  #不区分大小写
            dic[word.lower()] += 1
    #print dic

txt_dre= r"D:\file_py\Homework_HouLinjie\artical\aShortStory.txt"

get_word_frequencies(txt_dre)  
#读写文件路径：可以直接和执行文件放在一起，不用加路径，文件名即可，如果加路径，需要用/连接，而不是\连接