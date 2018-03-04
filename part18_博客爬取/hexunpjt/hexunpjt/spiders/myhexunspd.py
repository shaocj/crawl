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
    #编写首次爬取行为
    def start_requests(self):
        yield Request("url",headers="")
 #   start_urls = ['http://hexun.com/']

    def parse(self, response):
        item = HexunpjtItem()
        item['name'] = response.xpath("//span[@class='ArticleTitleTest']/a/text()").extract()
        item['url'] = response.xpath("//span[@class='ArticleTitleText']/a/@href").extract()
        #获取博文评论数和评论数
        #首先提取存储评论数和点击数的网址
        part1 = '<script type= "text/javascript" src="(http://click.tool.hexun.com/.*?)">'
        hcur1=re.compile(part1).findall(str(response.body))[0]
        headers2=()
        opener=urllib.request.build_opener()
        opener.addheaders=[headers2]
        urllib.request.install_opener(opener)
        data=urllib.request.urlopen(hcur1).read()
        #part2为提取文章阅读数的正则表达式
        #part3为提取文章评论数的正则表达式
        part2 = "click\d*?','(\d*?)'"
        part3="comment\d*?','(\d*?)'"
        item["hits"]=re.compile(part2).findall(str(data))
        item["comment"]=re.compile(part3).findall(str(data0))
        yield item
        #提取博文列表页的总页数
        part4="blog.hexun.com/p(.*?)/"
        #通过正则表达获取到的数据为一个列表，倒数第二个元素是总数
        data2=re.compile(part4).findall(str(response.body))
        if(len(data2)>=2):
            totalurl=data2[-2]
        else
            totalurl=1
            #进入for循环依次爬取各博文列表页的数据
        for i in range(2,int(totalurl)+1):
            #构造下一次要爬取的url，爬去一下页博文列表页中的数据
            nexturl="http://"+str(self.uid)+".blog.hexun.com/p"+str(i)+"default.html"
            #进行下一次爬去，模拟成浏览器进行
            yield Request(nexturl,callback=self.parse,headers={})
