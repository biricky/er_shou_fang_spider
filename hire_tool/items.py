# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HireToolItem(scrapy.Item):
    # define the fields for your item here like:
    xiaoqu = scrapy.Field()
    house_type = scrapy.Field()
    total_price = scrapy.Field()
    unit_price = scrapy.Field()
    jushi = scrapy.Field()
    house_area = scrapy.Field()
    subway_station = scrapy.Field()
    house_info = scrapy.Field()
