# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    garden = scrapy.Field()#门牌号
    region = scrapy.Field()#街道
    layout = scrapy.Field()#m室n厅
    size = scrapy.Field()#面积
    direction = scrapy.Field()#朝向
    renovation = scrapy.Field()#装修状况
    floor = scrapy.Field()#楼层
    year = scrapy.Field()#建成年份
    frame = scrapy.Field()#板楼 vs. 塔楼
    subway = scrapy.Field()#是否近地铁
    vr = scrapy.Field()#是否可以vr看房
    taxfree = scrapy.Field()#房本满几年
    haskey = scrapy.Field()#随时看房
    totalPrice = scrapy.Field()#总价
    unitPrice = scrapy.Field()#每平米单价
    
