# -*- coding: utf-8 -*-
import scrapy
import re
from news.items import NewsItem

class ToutiaoSpider(scrapy.Spider):
    name = 'toutiao'


    def __init__(self):
        self.allowed_domains = ['lf.snssdk.com']
        self.number = 0
        self.page = 0
        self.start_urls = ['https://lf.snssdk.com/article/v3/tab_comments/?group_id=6572339973414978051&aggr_type=1&count=20&offset=']

    def parse(self, response):
        html = response.text
        total_number = re.findall(r'"total_number":(\d+),',html)[0]
        text = re.findall(r'"text":"(.*?)",',html)
        user_name = re.findall(r'"user_name":"(.*?)"',html)

        for index in range(len(text)):
            item = NewsItem()
            item["text"] = text[index]
            item["user_name"] = user_name[index]
            self.number += 1
            yield item

        print(self.number,total_number)
        if self.number < int(total_number):
            self.page +=100
            url = self.start_urls[0]+str(self.page)
            print(url)
            yield scrapy.Request(url,callback=self.parse)