#coding=utf8
__author__ = 'zyx'

#利用TF/IDF算法统计出能代表各文档最重要的单词,并将各文档词频排序输出
import os
import jieba
import jieba.posseg as pseg
import sys
import string
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
reload(sys)
sys.setdefaultencoding('utf8')

#获取文件列表（该目录下放着4份文档）
def getFilelist(path):
    filelist = []
    files = os.listdir(path)
    for f in files :
        if(f[0] == '.'):
            pass
        else :
            filelist.append(f)
            print filelist
    return filelist,path

#对文档进行分词处理
def fenci(file_name,path) :
    #保存分词结果的目录
    sFilePath = './segfile'
    if not os.path.exists(sFilePath) :
        os.mkdir(sFilePath)
    #读取文档
    filename = file_name
    f = open(path+filename,'r+')
    file_list = f.read()
    f.close()

    #对文档进行分词处理，采用默认模式
    seg_list = jieba.cut(file_list,cut_all=True)

    #对空格，换行符进行处理
    result = []
    for seg in seg_list :
        seg = ''.join(seg.split())
        if (seg != '' and seg != "\n" and seg != "\n\n") :
            result.append(seg)

    #将分词后的结果用空格隔开，保存至本地。
    f = open(sFilePath+"/"+filename+"-seg.txt","w+")
    f.write(' '.join(result))
    f.close()

#读取已分词好的文档，进行TF-IDF计算
def Tfidf(filelist) :
    path = './segfile/'
    corpus = []  #存取文档的分词结果
    for ff in filelist :
        fname = path + ff+"-seg.txt"
        f = open(fname,'r+')
        content = f.read()
        f.close()
        corpus.append(content)

    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))

    word = vectorizer.get_feature_names() #所有文本的关键字
    weight = tfidf.toarray()              #对应的tfidf矩阵

    sFilePath = './tfidffile'
    if not os.path.exists(sFilePath) :
        os.mkdir(sFilePath)

    # 这里将每份文档词语的TF-IDF写入tfidffile文件夹中保存
    for i in range(len(weight)) :
        print u"--------Writing all the tf-idf in the",i,u" file into ",sFilePath+'/'+string.zfill(i,5)+'.txt',"--------"
        f = open(sFilePath+'/'+string.zfill(i,5)+'.txt','w+')
        for j in range(len(word)) :
            #f.write(word[j]+":"+str(weight[i][j])+"\n")
            f.write(word[j]+":"+str(weight[i][j])+"\n")
        f.close()

#循环输出每份文档内容并按tfidf值排序
def Output_tfidf(filename):
    f=open('./tfidffile/'+filename,'r')
    line = f.readlines()
    fre_sotrdict={}
    #将文本内容存入字典，以方便排序输出
    for i in range(len(line)):
        frelist=line[i]
        fre_sotrdict[frelist[0:frelist.index(":")]]=float(frelist[(frelist.index(":"))+1:len(frelist)-1])
    #输出词频
    WordValust_sort=sorted(fre_sotrdict.iteritems(),key=lambda d:d[1],reverse=True)
    for i in WordValust_sort:
        print i[0]+":%f"%i[1]

if __name__ == "__main__" :
    (allfile,path) = getFilelist('./file/')
    for ff in allfile :
        print "Using jieba on "+ff
        fenci(ff,path)

    #计算tfidf的函数
    Tfidf(allfile)

    #输出词频的函数
    files_tfidf = os.listdir('./tfidffile/')
    for filename in files_tfidf:
        print "-----------------------------------*这是",filename,"文档的词频输出*------------------------------------"
        Output_tfidf(filename)