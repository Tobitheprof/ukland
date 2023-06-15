# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CareereduItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class NewsItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    post_date = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()

class ApplicationItem(scrapy.Item):
    reference = scrapy.Field()
    application_validated = scrapy.Field()
    address = scrapy.Field()
    proposal = scrapy.Field()
    status = scrapy.Field()
    decision = scrapy.Field()
    decision_issue_date = scrapy.Field()
    appeal_status = scrapy.Field()
    appeal_decision = scrapy.Field()
    documents = scrapy.Field()
    cases = scrapy.Field()
    property = scrapy.Field()
