import scrapy
from scrapy import Selector
from collections import defaultdict

class KeysSpider(scrapy.Spider):
    name = "keywords"
    allowed_domains = ["*.lagou.com"]
    start_urls = [
        "http://www.lagou.com/"
        ]

    def parse(self,response):
        sel = Selector(response)
        keys = sel.xpath('//*[@class="menu_main job_hopping"]/h2/text()').extract()
        i = 1
        item = defaultdict(list)
        items = []
        for key in keys:
            if key.strip() != '':
                print "test"
                print key.strip()
                try:
                    print i
                    child_keys = sel.xpath('//*[@class="menu_box"][{}]/div[2]/dl/dt/a/text()'.format(i)).extract()
                    child_item = defaultdict(list)
                    for child_key in child_keys:
                        child_item[child_key.strip()].append(sel.xpath('//*[@class="menu_box"][{}]/div[2]/dl/dd/a/text()'.format(i)).extract())
                    item[key.strip()].append(child_item)
                except Exception, e:
                    print e
            else:
                continue
        yield item