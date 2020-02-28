import scrapy


class DateScrapperItem(scrapy.Item):
    url = scrapy.Field()
    copy_right = scrapy.Field()
    status_code = scrapy.Field()
