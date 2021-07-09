"""
第 0005 题： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
"""
# coding: utf-8

import os
import shutil

if __name__ =='__main__':
    sourcepath = r"D:\file_py\Homework_HouLinjie\artical\aShortStory.txt"
    distribution_path = r"D:\file_py\Homework_HouLinjie\artical\"    
    rs = unicode(sourcepath , "utf8")
    count = 1
    savepath =  unicode(distribution_path+"1", "utf-8")
    if not os.path.exists(savepath):
        os.makedirs(savepath)
    for rt,dirs,files in os.walk(rs):
        for fname in files:
            if ( count%10!=0 ):
                shutil.copy(rt + os.sep + fname,savepath) 
                #os.remove(rt + os.sep + fname)
            else:
                shutil.copy(rt + os.sep + fname,savepath) 
                #os.remove(rt + os.sep + fname)
                savepath =  unicode(distribution_path+str(count), "utf-8")
                if not os.path.exists(savepath):
                    os.makedirs(savepath)
            count+=1
