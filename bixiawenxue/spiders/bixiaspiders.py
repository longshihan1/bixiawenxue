import scrapy
from scrapy import Request
from scrapy.selector import HtmlXPathSelector

from bixiawenxue.items import BixiawenxueItem


class BaiHeSpider(scrapy.Spider):
    name = "bixiawenxue"
    start_urls = (
        'http://www.bxwx8.org/bsort/0/1.htm',
    )

    def parse(self, response):
        i=1
        for i in range(3):
            mainurl = 'http://www.bxwx8.org/bsort/0/' + str(i) + '.htm'
            yield Request(mainurl, callback=self.parse_url)

    def parse_url(self, response):
        response_selector = HtmlXPathSelector(response)
        items = response_selector.select(u'//tr/td[contains(@class, "odd")][1]/a/@href').extract()
        for item in items:
            main_item='http://www.bxwx8.org'+item
            yield Request(main_item, callback=self.parse_detail)


    def parse_detail(self, response):
        baihe_item = BixiawenxueItem()
        response_selector = HtmlXPathSelector(response)
        baihe_item['name']= response_selector.select(u'//strong/text()').extract()
        baihe_item['img'] = response_selector.select(u'//img[contains(@class, "picborder")]/@src').extract()

        baihe_item['type'] = response_selector.select(u'//table[contains(@cellpadding, "5")]/tr[1]/td[2]/a/text()').extract()
        baihe_item['url'] = response_selector.select(u'//input[contains(@name, "jumpurl")]/@value').extract()
        baihe_item['author'] = response_selector.select(u'//table[contains(@cellpadding, "5")]/tr[1]/td[4]/a/text()').extract()
        baihe_item['authoritem'] = response_selector.select(u'//table[contains(@cellpadding, "5")]/tr[1]/td[4]/a/@href').extract()
        baihe_item['bookstatus'] = response_selector.select(u'//table[contains(@cellpadding, "5")]/tr[2]/td[6]/text()').extract()
        baihe_item['count'] = response_selector.select(u'//table[contains(@cellpadding, "5")]/tr[3]/td[4]/text()').extract()
        baihe_item['introduction'] = response_selector.select(
            u'//div[@style="centerm"]/table[1]/tbody/tr/td/table[3]/tbody/tr/td/table[2]/tbody/tr/td/table/tbody/tr[2]/td[1]/div').extract()

        baihe_item['downloadurl'] = response_selector.select(u'/html/body/div[5]/div[@id="bxxinfo"]/div[@id="centerm"]/table[@id="download-box"]/tbody/tr/td/div[@class="block"]/div[@class="blockcontent"]/li[4]/a[@class="bdxz"]/@href').extract()

        baihe_item['bookitemlist']=response_selector.select(u'/html/body/div[5]/div[@id="bxxinfo"]/div[@id="centerm"]/table[1]/tbody/tr/td/table[3]/tbody/tr/td/table[1]/tbody/tr/td[1]/table/tbody/tr/td/a]/@href').extract()


        yield baihe_item
