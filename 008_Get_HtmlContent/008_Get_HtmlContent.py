#coding=utf-8
__author__ = 'zyx'

import urllib2
from bs4 import BeautifulSoup

url = "http://www.ce.cn/xwzx/gnsz/szyw/201610/18/t20161018_16903079.shtml"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page)
for link in soup.find_all('p'):
    print link.get_text
