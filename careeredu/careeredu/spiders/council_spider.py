import scrapy
from urllib.parse import urlencode

class PlanningSpider(scrapy.Spider):
    name = "planning"
    allowed_domains = ["pa.canterbury.gov.uk"]
    start_urls = ["https://pa.canterbury.gov.uk/online-applications/search.do?action=advanced"]





    def parse(self, response):
        # Scrape the planning application data
        token = response.css('input[name="_csrf"]::attr(value)').extract_first()
        data = {
            '_csrf' : token,
            'searchCriteria.address' : 'plan',
            'date(applicationValidatedEnd)' : '12/06/2023',
            'date(applicationValidatedStart)' : '01/10/1974'
        }
        yield scrapy.FormRequest.from_response(response, formdata=data, callback=self.parse_council)

    def parse_council(self, response):
        for q in response.css('#searchResultsContainer'):
            yield {
                'url' : q.css('.searchresult a::text').getall()
            }

