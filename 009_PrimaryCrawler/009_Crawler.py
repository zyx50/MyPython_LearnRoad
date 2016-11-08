#coding=utf8
__author__ = 'zyx'

#urllib2下载网页的三种方法
import urllib2,cookielib
from bs4 import BeautifulSoup
import urlparse

url="http://www.baidu.com"
print '第一种方法'
response1=urllib2.urlopen(url)
print response1.getcode()
print len(response1.read())

print "第二种方法"
request=urllib2.Request(url)
request.add_header("user-agent","Mozilla/5.0")
response2=urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())

print "第三种方法"
cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3=urllib2.urlopen(url)
print response3.getcode()
print cj
text=response3.read()
soup1=BeautifulSoup(text,'html.parser',from_encoding='utf-8')
print '获取所有的链接'
links=soup1.find_all('a')
for link in links:
    print link.name,link['href'],link.get_text()
print '获取某一个url链接'
link_node=soup1.find('a',href='http://home.baidu.com')
print link_node.name,link_node['href'],link_node.get_text()



root_url="http://newhouse.hz.fang.com/house/s/b81-b91/?ctm=1.hz.xf_search.page.1"
new_url="/house/s/b81-b932/"
new_full_url=urlparse.urljoin(root_url,new_url)
print new_full_url

