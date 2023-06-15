import scrapy


class AdikaspiderSpider(scrapy.Spider):
    name = "adikaspider"
    allowed_domains = ["flutterwave.com"]
    start_urls = ["https://flutterwave.com/store/adikastakes"]

    def parse(self, response):
        pass
