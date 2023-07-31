#参见：https://docs.scrapy.org/en/latest/intro/tutorial.html
import scrapy
import json
 
from lianjia.items import LianjiaItem
 
class LianjiaSpider(scrapy.Spider):
    name = "lianjia"
    allowed_domains = ["bj.lianjia.com"]
    start_urls = [
        "https://bj.lianjia.com/ershoufang/dongcheng/",
        "https://bj.lianjia.com/ershoufang/xicheng/",
        "https://bj.lianjia.com/ershoufang/chaoyang/",
        "https://bj.lianjia.com/ershoufang/haidian/",
        "https://bj.lianjia.com/ershoufang/fengtai/",
        "https://bj.lianjia.com/ershoufang/shijingshan/",
        "https://bj.lianjia.com/ershoufang/tongzhou/",
        "https://bj.lianjia.com/ershoufang/changping/",
        "https://bj.lianjia.com/ershoufang/daxing/",
        "https://bj.lianjia.com/ershoufang/yizhuangkaifaqu/",
        "https://bj.lianjia.com/ershoufang/shunyi/",
        "https://bj.lianjia.com/ershoufang/fangshan/",
        "https://bj.lianjia.com/ershoufang/mentougou/",
        "https://bj.lianjia.com/ershoufang/pinggu/",
        "https://bj.lianjia.com/ershoufang/huairou/",
        "https://bj.lianjia.com/ershoufang/miyun/",
        "https://bj.lianjia.com/ershoufang/yanqing/"
    ]
 
    def parse(self, response):
        sel = scrapy.selector.Selector(response)
        
        #sites = sel.xpath('/html/body/div[@class="content"]/div[@class="leftContent"]/ul[@class="sellListContent"]/li[@class="clear LOGCLICKDATA"]/div[@class="info clear"]')
        sites = sel.xpath('//div[@class="info clear"]')

        # items = []
        for site in sites:
            item = LianjiaItem()
            #使用特征定位
            #extract()的结果是字符串列表，但是在生成csv或json文件时会自动转化为extract()[0]
            #但若要对字符串进行处理，例如删去"114平米"中的"平米"，则需要索引到extract()[0]再对字符串进行操作，参见第34,38,45行
            item['garden'] = site.xpath('div[@class="flood"]/div[@class="positionInfo"]/a[contains(@href,"xiaoqu")]/text()').extract()
            item['region'] = site.xpath('div[@class="flood"]/div[@class="positionInfo"]/a[contains(@href,"ershoufang")]/text()').extract()
            #使用索引定位：可在浏览器中选中html复制xpath获得
            #item['garden'] = site.xpath('div[2]/div[1]/a[1]/text()').extract()
            #item['region'] = site.xpath('div[2]/div[1]/a[2]/text()').extract()

            
            houseInfo_str = site.xpath('div[@class="address"]/div[@class="houseInfo"]/text()').extract()[0]#如：1室1厅 | 44.64平米 | 南 | 简装 | 中楼层(共18层) | 1993年建 | 塔楼
            splited_houseInfo_str_list = houseInfo_str.split(" | ")#以" | "为间隔将houseInfo_str拆分
            
            item['layout'] = splited_houseInfo_str_list[0]
            item['size'] = (splited_houseInfo_str_list[1])[:-2]# 删去44.64后的"平米"
            item['direction'] = splited_houseInfo_str_list[2]
            item['renovation'] = splited_houseInfo_str_list[3]
            
            if (len(splited_houseInfo_str_list) > 4): #1室1厅 | 44.64平米 | 南 | 简装 以外的情形
                item['floor'] = splited_houseInfo_str_list[4]
            if (len(splited_houseInfo_str_list) > 5):
                item['year'] = (splited_houseInfo_str_list[5])[:-2]# 删去1993后的"年建"
            
            if (len(splited_houseInfo_str_list) > 7):#排除此类情形：1室1厅 | 44.64平米 | 南 | 简装 | 中楼层(共18层) | 1993年建 | 暂无数据 | 联排别墅
                item['frame'] = splited_houseInfo_str_list[7]
            elif (len(splited_houseInfo_str_list) > 6):
                item['frame'] = splited_houseInfo_str_list[6]
            else:
                pass
            
            item['subway'] = site.xpath('div[@class="tag"]/span[@class="subway"]/text()').extract()
            item['vr'] = site.xpath('div[@class="tag"]/span[@class="isVrFutureHome"]/text()').extract()
            item['taxfree'] = site.xpath('div[@class="tag"]/span[@class="taxfree"]/text()').extract()
            item['haskey'] = site.xpath('div[@class="tag"]/span[@class="haskey"]/text()').extract()
            
            item['totalPrice'] = site.xpath('div[@class="priceInfo"]/div[@class="totalPrice"]/span/text()').extract()
            item['unitPrice'] = site.xpath('div[@class="priceInfo"]/div[@class="unitPrice"]/@data-price').extract()
            
            print(item)
            yield(item)
            
        page_info_html = sel.xpath('/html/body/div[4]/div[1]/div[8]/div[2]/div')
        page_url = page_info_html.xpath('@page-url').extract()[0]
        page_data_json = page_info_html.xpath('@page-data').extract()[0]
        page_data_dic = json.loads(page_data_json)
            
        if (page_data_dic["totalPage"] > page_data_dic["curPage"]):
            #urljoin()方法构建一个完整的绝对 URL （因为链接可以是相对的）并产生对下一页的新请求
            #next_page = response.urljoin("".join(["https://bj.lianjia.com",page_url.rsplit("{",1)[0],str(page_data_dic["curPage"] + 1)]))
            next_page = "".join(["https://bj.lianjia.com",page_url.rsplit("{",1)[0],str(page_data_dic["curPage"] + 1)])
            yield scrapy.Request(next_page, callback=self.parse ,dont_filter=True)
        
        # return items