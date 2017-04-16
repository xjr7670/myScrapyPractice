# -*- coding: utf-8 -*-
import scrapy
from scrapy_env.items import ScrapyEnvItem

class sitemapSpider(scrapy.Spider):
    name = "Get_url"
    allowed_domains = ['niukou.space']
    start_urls = ['http://www.niukou.space']

    def parse(self, response):
        a_list = response.xpath('//a/@href').extract()
        for a in a_list:
            item = ScrapyEnvItem()
            item['url'] = a
            yield item

        for url in response.xpath('//a/@href').extract():
            yield scrapy.Request(url, callback=self.parse)