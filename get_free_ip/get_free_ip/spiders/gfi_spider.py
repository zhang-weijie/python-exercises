import scrapy
from get_free_ip.items import GFIItem

class GetFreeIpSpider(scrapy.Spider):
    name='gfi'
    allowed_domains=['cn-proxy.com']
    start_urls=['http://cn-proxy.com/']

    def parse(self,response):
        sel=scrapy.selector.Selector(response)
        sites=sel.xpath('//div[@class="table-container"]/table/tbody/tr')
        items=[]
        for site in sites:
            item=GFIItem()
            infoList=site.xpath('td/text()').extract()
            item['server_addr']=infoList[0]
            item['port_code']=infoList[1]
            item['server_place']=infoList[2]
            item['last_check_time']=infoList[5]
            items.append(item)
        return items
            
            
