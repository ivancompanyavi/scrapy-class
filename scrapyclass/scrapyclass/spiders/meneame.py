from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from scrapyclass.items import MeneameItem


class MeneameSpider(CrawlSpider):
    name = 'meneame'

    start_urls = ['http://meneame.net']

    rules = (
        Rule(LinkExtractor(allow='\?page=\d+')),
        Rule(LinkExtractor(allow='meneame.net/story'), callback='parse_article'),
    )

    def parse_article(self, response):
        item = MeneameItem()
        item['title'] = response.css('.news-body h1 a::text').extract()[0]
        item['description'] = response.css('.news-body::text').extract()[4]

        return item