import scrapy
from careeredu.items import NewsItem


class JobspiderSpider(scrapy.Spider):
    name = "jobspider"
    allowed_domains = ["punchng.com"]
    start_urls = ["https://punchng.com/topics/news/"]

    def parse(self, response):
        news = response.css('section .category-section-2')
        for update in news:

            relative_url = update.css('.post-title a::attr(href)').get()


            yield response.follow(relative_url, callback=self.parse_news_page)


        next_page = response.css(".next::attr(href)").get()
        if next_page is not None:
            next_page_url = next_page

            yield response.follow(next_page_url, callback=self.parse)

    def parse_news_page(self, response):

        news_item = NewsItem()
    
        news_item['url'] = response.url
        news_item['title'] = response.css(".post-title a::text").get()
        news_item['post_date'] = response.css(".post-date::text").get()
        news_item['author'] = response.css(".post-author a::text").get()
        news_item['content'] = response.css(".post-content p::text").getall()
        
        yield news_item
