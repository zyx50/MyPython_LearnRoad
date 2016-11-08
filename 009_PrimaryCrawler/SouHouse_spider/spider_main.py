# coding=utf-8
__author__ = 'zyx'

import url_manager,html_downloader,html_parser,html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls=url_manager.UrlManager()#管理URL
        self.downloader=html_downloader.HtmlDownloader()#下载URL内容
        self.parser=html_parser.HtmlParser()#解析URL内容
        self.outputer=html_outputer.HtmlOutputer()#输出获取到的内容

    #获取待爬取城市链接
    def CityUrl_Crwa(self,root_url):
        html_cont=self.downloader.download(root_url)
        cityurls_list=self.parser.cityurlparser(html_cont)
        return cityurls_list

    #爬虫主体程序
    def crwa(self,city_url):
        count=0
        self.urls.add_new_url(city_url)#将根链接首先放入url列表
        while self.urls.has_new_url():
            count=count+1
            try:
                new_url=self.urls.get_new_url()#获取新的链接
                html_cont=self.downloader.download(new_url)#下载页面内容
                new_urls, new_data ,house_city= self.parser.parse(new_url, html_cont)#解析页面内容
                self.urls.add_new_urls(new_urls)
                self.outputer.output_excel(new_data,house_city)#写入excel
                #self.outputer.output_mysql(new_data,house_city)#写入mysql
                print "第",count,"个网页【",new_url,"】输出成功--------------"
            except:
                self.urls.add_false_url(new_url)
                print "第",count,"个网页【",new_url,"】爬取失败，将会被重新爬取,失败次数过多将会被舍弃-------------"
                count=count-1
        self.urls.release_urllist()




if __name__=="__main__":
    obj_spider=SpiderMain()
    root_url="http://newhouse.wuhan.fang.com/house/s/b81-b91/"
    city_urls=obj_spider.CityUrl_Crwa(root_url)
    for city_url in city_urls:
        obj_spider.crwa(city_url)