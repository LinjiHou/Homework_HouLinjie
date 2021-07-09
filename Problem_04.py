"""
第 0004 题： 任一个英文的纯文本文件，统计其中的单词出现的个数。
"""
#读写文件路径：如果加路径，需要用/连接，而不是\连接
import re
import chardet   #需要导入这个模块，检测编码格式  

def get_word_frequencies(file_place):
    with open(file_place,'rb') as txt: #打开文件，记作f
        txt = txt.read().decode('utf-8')
    txt = re.sub(r'[.?!,""/]', ' ', txt)   #要替换的标点符号，英文字符可能出现的    
    
    dic = {}
    txt = txt.splitlines() 
    for line in txt:
        for word in line.split():
            dic.setdefault(word.lower(), 0)  #不区分大小写
            dic[word.lower()] += 1
    
    return dic

if __name__ == "__main__":
    txt_dre= r"D:\file_py\Homework_HouLinjie\artical\aShortStory.txt"
    dic = get_word_frequencies(txt_dre)  
    
    for x, y in dic.items():
        print(x, y)
    print('文本共出现了%s个不同的单词', len(dic))
