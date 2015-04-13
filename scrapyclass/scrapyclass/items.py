# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class MeneameItem(Item):

    title = Field()
    description = Field()


class TwitterItem(Item):

    date = Field()
    tweet = Field()


class SerieslyItem(Item):

    title = Field()
