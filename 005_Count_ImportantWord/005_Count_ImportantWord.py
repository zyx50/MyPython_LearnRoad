#coding=utf-8
__author__ = 'zyx'

#利用TF/IDF算法统计出能代表各文档最重要的单词
import re,MySQLdb,os,math

def count_word (filepath,i):
    file=open(filepath,'r')
    file_content=file.read()
    CountWord=re.findall(r'[a-zA-Z0-9]+',file_content)
    print "第%d篇文章的单词内容为：%s"%(i,CountWord)
    print "第%d篇文章的单词总量为：%d"%(i,len(CountWord))

#统计词频，并插入数据库
    CountWord_only=list(set(CountWord))
    print "第%d篇文章的单词正在写入数据库（loading......）"%(i)
    #将单词和词频放入数据库中
    for n in range(len(CountWord_only)):
        CountWord_only_valuse=CountWord.count(CountWord_only[n])
        cursor.execute("insert into TFIDF (fileno,word,wordfre) values('%s','%s','%s')"%(str(i),CountWord_only[n],CountWord_only_valuse))
        db.commit()
    print "第%d篇文章的单词写入数据库成功（successful）"%(i)

def tfidf():
    #查询单词总数
    cursor.execute("SELECT sum(wordfre) FROM tfidf group by fileno")
    results_fretotal =cursor.fetchall()
   #查询单词记录
    cursor.execute("SELECT fileno,word,wordfre FROM tfidf")
    results_freword=cursor.fetchall()
    #查询
    wordfre_sum=0
    #计算单词总数
    for m in range(len(results_fretotal)):
        wordfre_sum=results_fretotal[m][0]+wordfre_sum
    #计算每一个单词的频率tf
    for m in range(len(results_freword)):
        fre_everyword=long(results_freword[m][2])/float(wordfre_sum)
        cursor.execute("update TFIDF set tf=%f where fileno='%s' and word='%s'"%(fre_everyword,str(long(results_freword[m][0])),str((results_freword[m][1]))))
        db.commit()

    #计算IDF
    cursor.execute("SELECT word,count(word) FROM tfidf GROUP BY word")#查询包含该词的文档数
    results_paperword=cursor.fetchall()
    for v in range(len(results_paperword)):
        idf=math.log(float(len(file_total))/results_paperword[v][1]+1)
        cursor.execute("update TFIDF set idf=%f where word='%s'"%(idf,str(results_paperword[v][0])))
        db.commit()

    #计算tf*idf
    cursor.execute("SELECT fileno,word,tf*idf from tfidf")
    results_select_tfidf=cursor.fetchall()
    for v in range(len(results_select_tfidf)):
        cursor.execute("update TFIDF set tfidf=%f where fileno='%s' and word='%s'"%(results_select_tfidf[v][2],str(results_select_tfidf[v][0]),str(results_select_tfidf[v][1])))
        print results_select_tfidf[v][0],"：",results_select_tfidf[v][1]," ",results_select_tfidf[v][2]
        db.commit()

if __name__=='__main__':
    file_total=os.listdir('./file')
    print "计算中请稍后（loading......）"
    # 打开数据库连接，使用cursor()方法获取操作游标
    db=MySQLdb.connect("localhost","root","root","test")
    cursor=db.cursor()
    cursor.execute("Truncate Table TFIDF")
    #读取文档
    for i in range(len(file_total)):
        count_word("file/%s"% file_total[i],i+1)

    tfidf()
    db.close()



