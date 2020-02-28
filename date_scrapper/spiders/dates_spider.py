import scrapy

from date_scrapper.items import DateScrapperItem


class DatesSpider(scrapy.Spider):
    name = 'dates'

    def __init__(self, csv_path):
        self.csv_path = csv_path
        super().__init__()

    def start_requests(self):
        with open(self.csv_path, 'r') as csf_file:
            for url in csf_file.readlines()[1:5000]:
                url = url.strip()
                yield scrapy.Request(url, callback=self.parse, meta={'url': url})

    def parse(self, response):
        footer_date = None
        footer = response.xpath('//footer//text()')
        if footer:
            match = footer.re(r'©[ \t\n]*(\d{4})(?:[ \t\n-–]+(\d{4}))?')
            if match:
                if not match[1]:
                    footer_date = int(match[0])
                else:
                    footer_date = int(match[1])
        item = DateScrapperItem()
        item['url'] = response.meta['url']
        item['copy_right'] = footer_date
        item['status_code'] = response.status
        yield item
