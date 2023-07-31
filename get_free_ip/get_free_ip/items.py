# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GFIItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    server_addr=scrapy.Field()
    port_code=scrapy.Field()
    server_place=scrapy.Field()
    last_check_time=scrapy.Field()
