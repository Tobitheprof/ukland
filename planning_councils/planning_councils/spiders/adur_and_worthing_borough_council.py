import scrapy


class AdurAndWorthingBoroughCouncilSpider(scrapy.Spider):
    name = "adur_and_worthing_borough_council"
    allowed_domains = ["adur-worthing.gov.uk"]
    start_urls = ["https://adur-worthing.gov.uk"]

    def parse(self, response):
        pass
