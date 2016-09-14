#-*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from hire_tool.items import HireToolItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["lianjia.com"]
    start_urls = ["http://bj.lianjia.com/ershoufang/chaoyang/pg%s" % str(i) for i in range(100) ]
    start_urls.append("http://bj.lianjia.com/ershoufang/chaoyang")
    #start_urls = [
    #    "http://bj.lianjia.com/ershoufang/chaoyang/"
    #]
    #rules = (
    #    Rule(SgmlLinkExtractor(allow=('ershoufang/chaoyang/pg[0-9]/', )), callback='parse'),
    #    Rule(SgmlLinkExtractor(allow=('ershoufang/chaoyang/pg[0-9]/', ), )),
    #)

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//li[@class=\'clear\']')
        items = []
        for site in sites:
            item = HireToolItem()
            item['xiaoqu'] = site.xpath('./div[@class=\'info clear\']/div[@class=\'address\']/div[@class=\'houseInfo\']/a/text()').extract()
            item['house_info'] = site.xpath('./div[@class=\'info clear\']/div[@class=\'address\']/div[@class=\'houseInfo\']/text()').extract()
            item['total_price'] = site.xpath('./div[@class=\'info clear\']/div[@class=\'priceInfo\']/div[@class=\'totalPrice\']/span/text()').extract()
            item['unit_price'] = site.xpath('./div[@class=\'info clear\']/div[@class=\'priceInfo\']/div[@class=\'unitPrice\']/span/text()').extract()
            item['subway_station'] = site.xpath('./div[@class=\'info clear\']/div[@class=\'tag\']/span[@class=\'subway\']/text()').extract()
            item['xiaoqu'] = [x.encode('utf-8') for x in item['xiaoqu']]
            item['house_info'] = [h.encode('utf-8') for h in item['house_info']]
            item['total_price'] = [tp.encode('utf-8') for tp in item['total_price']]
            item['unit_price'] = [up.encode('utf-8') for up in item['unit_price']]
            item['subway_station'] = [ss.encode('utf-8') for ss in item['subway_station']]
            items.append(item)

        return items

