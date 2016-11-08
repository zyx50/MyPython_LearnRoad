#coding=utf-8
__author__ = 'zyx'

#有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
import os

#查找目录及其子目录下所有的文件

total=[]#定义全局变量，用于存储每个文件得到的代码行数
def findfile(path):
    dirs = os.listdir(path)
    for filename in dirs:
        if os.path.isdir((path+'\\'+filename)):
            findfile(path+'\\'+filename)
        else:
            if os.path.isfile((path+'\\'+filename)) and filename.find('.py')!=-1:
                print '这是文件',filename,"的代码行数"
                code_len=count_code(path+'\\'+filename)
                total.append(code_len)

#计算总代码行、空行和注释行
def count_code(file_name):
    file_code=open(file_name,'r')
    file_codelist=file_code.readlines()
    #计算注释行
    explanatory=0
    for code in file_codelist:
        if '#' in code:
            explanatory=explanatory+1
    print '该文件总代码行数为：',len(file_codelist)
    print '空行数为：',file_codelist.count('\n')
    print '注释行数为：',explanatory
    return len(file_codelist)
    file_code.close()


if __name__=="__main__":
    findfile('E:\MyPythonPro\study_file')
    print '所有文件代码行数为：',sum(total)

