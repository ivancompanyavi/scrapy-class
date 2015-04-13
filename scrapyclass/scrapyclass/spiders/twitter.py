import datetime

import scrapy

from scrapyclass.items import TwitterItem

NUMBER_OF_TWEETS = 10


class TwitterSpider(scrapy.Spider):
    name = 'twitter'

    def __init__(self, username=''):
        self.start_urls = ['https://twitter.com/' + username]
        super(TwitterSpider, self).__init__()

    def parse(self, response):
        tweets = response.xpath('//div[@data-component-term="tweet"]')
        tweets = tweets[:NUMBER_OF_TWEETS] if len(tweets) <= NUMBER_OF_TWEETS else tweets
        for tweet in tweets:
            item = TwitterItem()
            item['tweet'] = tweet.xpath('.//p/text()').extract()[0]
            date_timestamp = tweet.xpath('.//span[@data-time]/@data-time').extract()[0]
            item['date'] = datetime.datetime.fromtimestamp(int(date_timestamp)).strftime('%Y-%m-%d %H:%M:%S')
            yield item
