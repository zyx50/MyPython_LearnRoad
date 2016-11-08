#coding=utf-8
__author__ = 'zyx'

#任一个英文的纯文本文件，统计其中的单词出现的个数及各单词的词频倒序。
import re

#统计单词个数
def count_word (filepath):
    file=open(filepath,'r')
    file_content=file.read()
    CountWord=re.findall(r'[a-zA-Z]+',file_content)
    print "单词内容为：",(CountWord)
    print "单词总量为：",(len(CountWord))

    #统计词频
    CountWord_only=list(set(CountWord))
    print "下面是每一个单词的词频："
    #将单词和词频放入一个字典中
    WordValust={}
    for i in range(len(CountWord_only)):
        CountWord_only_valuse=CountWord.count(CountWord_only[i])
        WordValust[CountWord_only[i]]=CountWord_only_valuse #dic[key]=valuse

    #输出词频的倒序
    WordValust_sort=sorted(WordValust.iteritems(),key=lambda d:d[1],reverse=True)
    for i in WordValust_sort:
        print i[0]+":%d"%(i[1])

    file.close()

if __name__=='__main__':
    count_word("i have a dream.txt")