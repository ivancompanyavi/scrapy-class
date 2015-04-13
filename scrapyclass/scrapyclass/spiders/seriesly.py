import scrapy
from scrapyclass.items import SerieslyItem

class SerieslySpider(scrapy.Spider):

    name = 'seriesly'

    def __init__(self, username, password):
        self.username = username
        self.password = password
        super(SerieslySpider, self).__init__()

    def start_requests(self):
        return [scrapy.FormRequest('http://series.ly/scripts/login/login.php',
                                   formdata={'lg_login': self.username, 'lg_pass': self.password},
                                   callback=self.parse_main_page)]

    def parse_main_page(self, response):
        return scrapy.Request('http://series.ly/@' + self.username + '/_series', callback=self.parse_profile)

    def parse_profile(self, response):
        profile_uid = response.css('#profileUID').xpath('@value').extract()[0]
        yield scrapy.Request(
            'http://series.ly/perfil/subperfil/series.php?uid={}&id={}'.format(profile_uid, profile_uid),
            callback=self.parse_series)

    def parse_series(self, response):
        series = response.xpath('//div[contains(@class, "searchResult")]')
        for serie in series:
            item = SerieslyItem()
            item['title'] = serie.css('.tituloAct::text').extract()[0]
            yield item



