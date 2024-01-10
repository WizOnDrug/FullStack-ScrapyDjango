from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


import scrapy

class JabamaSpider(CrawlSpider):
    name = "jabama"
    allowed_domains = ["jabama.com"]
    start_urls = ['https://www.jabama.com/']

    rules = (
        Rule(LinkExtractor(allow="city-tehran")),
        Rule(LinkExtractor(allow="stay"), callback="parse_item")
    )

    def parse_item(self, response):
            if 'stay' in response.url:
                yield {
                    "title": response.css('h1::text').get().strip(),
                    "price": response.css(".accommodation-pdp-sidebar-info-price-amount__price::text").get().strip(),
                    "description": response.css(".accommodation-pdp-specification-description__item::text")[1:].get().strip(),
                    "image_links": [img.css('img::attr(src)').extract_first() for img in response.css('.gallery-img')]
                }


