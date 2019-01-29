# -*- coding: utf-8 -*-
import scrapy

from dingdong.items import DingdongItem


class CrawlDingdongArticleSpider(scrapy.Spider):
    name = 'crawl_dingdong_article'
    allowed_domains = ['www.thepaper.cn']
    url='https://www.thepaper.cn/load_index.jsp?nodeids=25490&topCids=&pageidx='
    # 设置页码
    offset = 1
    start_urls = [url+str(offset)+'&isList=true']
    def parse(self, response):

        for each in response.xpath("//div[@class='news_li']"):
            item=DingdongItem()
            item["article"] = each.xpath("./h2/a/text()").extract()[0]
            item["imgurl"] = each.xpath("./div[1]/a/img/@src").extract()[0]


            yield item

        if (self.offset < 3):
            self.offset += 1
        # 将请求交给控制器
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)