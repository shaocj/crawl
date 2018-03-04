# -*- coding: utf-8 -*-
import scrapy
import re
import urllib.request
from hexunpjt.items import HexunpjtItem
from scrapy.http import Request

class MyhexunspdSpider(scrapy.Spider):
    name = 'myhexunspd'
    allowed_domains = ['hexun.com']
    # 设置要爬屈用户的
    uid = "27636918"
    def start_requests(self):
        yield Request("url",headers="")
 #   start_urls = ['http://hexun.com/']

    def parse(self, response):
        item = HexunpjtItem()
        item['name'] = response.xpath("//span[@class='ArticleTitleTest']/a/text()").extract()
        item['url'] = response.xpath("//span[@class='ArticleTitleText']/a/@href").extract()
        part1 = '<script type= "text/javascript" src="(http://click.tool.hexun.com/.*?)">'
        hcur1=re.compile(part1).findall(str(response.body))[0]
        headers2=()
        opener=urllib.request.build_opener()
        opener.addheaders=[headers2]
        urllib.request.install_opener(opener)
        data=urllib.request.urlopen(hcur1).read()
        part3 = "click\d*?','(\d*?)'"
        part3="comment\d*?','(\d*?)'"
        item["hits"]=re.compile(part2).findall(str(data))
        item["comment"]=re.compile(part3).findall(str(data0))
        yield item
        part4="blog.hexun.com/p(.*?)/"
        data2=re.compile(part4).findall(str(response.body))
        if(len(data2)>=2):
            totalurl=data2[-2]
        else
            totalurl=1
        for i in range(2,int(totalurl)+1):
            nexturl="http://"+str(self.uid)+".blog.hexun.com/p"+str(i)+"default.html"
            yield Request(nexturl,callback=self.parse,headers={})