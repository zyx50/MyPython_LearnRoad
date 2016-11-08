# coding=utf-8
__author__ = 'zyx'
import requests


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        html=requests.get(url)
        html=html.text.encode(html.encoding).decode("gbk").encode("utf8")
        return html


