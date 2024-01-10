# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import scrapy


class DivarScrapperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    area=scrapy.Field()
    construction_year=scrapy.Field()
    rooms=scrapy.Field()
    total_price=scrapy.Field()
    floor=scrapy.Field()
    elevator=scrapy.Field()
    parking=scrapy.Field()
    warehouse=scrapy.Field()
    price=scrapy.Field()
    token=scrapy.Field()