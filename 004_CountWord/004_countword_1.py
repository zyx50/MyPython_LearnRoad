#-*-coding: utf-8-*-
#任一个英文的纯文本文件，统计其中的单词出现的个数。
import re
def countword(filepath):
    f=open(filepath)
    all_the_text=f.read().lower()
    word_content={}
    all_the_text=re.findall(r'\w+',all_the_text)

    for word in all_the_text:
        if word in word_content:
            word_content[word]+=1
        else:
            word_content[word]=1
    print '单词出现次数为:',len(all_the_text)
    print '初始词频统计结果为:'
    print word_content.items()

#按照词频排序
    print '按照词频排序:'
    print sorted(word_content.iteritems(),key=lambda d:d[1],reverse=True) #通过key参数指定排序为value,逆序排列

#按照首字母排序
    print '按照首字母排序:'
    print sorted(word_content.iteritems(),key=lambda d:d[0])

#按照首字母排序方式2
    print '按照首字母排序方式2:'
    print sorted(word_content.iteritems(),lambda x,y:cmp(x,y))

    f.close()

if __name__=='__main__':
    countword('i have a dream.txt')


