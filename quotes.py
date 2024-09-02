import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            text = quote.css('span.text::text').get()
            author = quote.css('span small.author::text').get()
            tags = quote.css('div.tags a.tag::text').getall()

            yield {
                'text': text,
                'author': author,
                'tags': tags
            }

        for author_link in response.css('div.quote span a::attr(href)').getall():
            yield response.follow(author_link, self.parse_author)

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_author(self, response):
        name = response.css('h3.author-title::text').get().strip()
        birth_date = response.css('span.author-born-date::text').get()
        birth_place = response.css('span.author-born-location::text').get().strip("in ")
        description = response.css('div.author-description::text').get().strip()

        yield {
            'author': name,
            'birth_date': birth_date,
            'birth_place': birth_place,
            'description': description
        }
