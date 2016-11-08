#-*-coding: utf-8-*-

#爬取百度贴吧图片
import urllib2
import re
req=urllib2.urlopen('http://www.imooc.com/search/course?words=python')
buf=req.read() #读取url内容
url_lst=re.findall(r'http:.+.jpg',buf) #提取图片url
i=0
for url in url_lst:
    f=open('.\pic\\'+str(i)+'.jpg','w') #以写方式打开，只能写文件，如果文件不存在，创建该文件如果文件已存在，先清空，再打开文件
    req=urllib2.urlopen(url) #打开每个图片url
    buf=req.read() #读入文件
    f.write(buf) #将字符串写入文件，没有返回值。
    i+=1

