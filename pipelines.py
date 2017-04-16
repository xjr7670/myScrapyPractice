# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
from urllib import parse

from scrapy.exceptions import DropItem
from .spiders.get_sitemap import sitemapSpider

class ScrapyEnvPipeline(object):

    def __init__(self):
        self.url_set = set()
        self.pat_rpl = re.compile(r'#.+')
        self.pat_domain = re.compile(r'\.(.+.com)')
        self.domains = sitemapSpider().allowed_domains

    def process_item(self, item, spider):
        #item_domain = self.pat_domain.search(item['url']).groups(0)[0]
        item['url'] = self.pat_rpl.sub("", item['url'])
        if item['url'] in self.url_set:
            raise DropItem("Found duplicate %s" % item['url'])
        elif 'niukou.space' not in item['url']:
            raise DropItem("Not my website")
        else:
            self.url_set.add(item['url'])
            return item
