import scrapy
from scrapy_selenium import SeleniumRequest



class AshfieldSpider(scrapy.Spider):
    name = "ashfield"
    allowed_domains = ["planning.ashfield.gov.uk"]
    start_urls = ["https://planning.ashfield.gov.uk/planning-applications/search-applications/?civica.query.SDate1From=21%2F05%2F2023&civica.query.SDate1To=27%2F05%2F2023"]


    def start_requests(self):
        url = 'https://planning.ashfield.gov.uk/planning-applications/search-applications/?civica.query.SDate1From=21%2F05%2F2023&civica.query.SDate1To=27%2F05%2F2023'
        yield SeleniumRequest(url=url, callback=self.parse, wait_time=10)


    def parse(self, response):
        text = response.css("#civica-result264")
        for t in text:
            yield{
                'name' : t.css(".civica-gfplanning-internetdesc")
            }
