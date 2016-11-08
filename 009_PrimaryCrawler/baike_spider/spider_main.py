#coding=utf8
__author__ = 'zyx'

import url_manager,html_downloader,html_parser,html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls=url_manager.UrlManager()#管理URL
        self.downloader=html_downloader.HtmlDownloader()#下载URL内容
        self.parser=html_parser.HtmlParser()#解析URL内容
        self.outputer=html_outputer.HtmlOutputer()#输出获取到的内容到html页面

    #爬虫主体程序
    def craw(self,root_url):
        count =1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url=self.urls.get_new_url()
                print 'craw %d:%s'%(count,new_url)
                html_cont=self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count==2:
                    break
                count=count + 1
            except:
                print 'craw failed'


        self.outputer.output_html()



if __name__=="__main__":
    root_url="http://baike.baidu.com/view/21087.htm"
    obj_spider=SpiderMain()
    obj_spider.craw(root_url)
