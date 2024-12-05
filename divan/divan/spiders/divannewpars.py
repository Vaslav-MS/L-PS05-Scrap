import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/ekaterinburg/category/svet"]

    def parse(self, response):
#       divans = response.css('div._Ud0k')
        svetis = response.css('div.LlPhw')
        for svet in svetis:
            yield {
#               'name' : divan.css('div.lsooF span::text').get(),
#               'price': divan.css('div.q5Uds span::text').get(),
#               'url': divan.css('a').attrib['href']
                'name': svet.css('div.lsooF span::text').get(),
                'price': svet.css('div.q5Uds span::text').get(),
                'url': svet.css('a').attrib['href']
            }
