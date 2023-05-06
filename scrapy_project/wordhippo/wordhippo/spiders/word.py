import scrapy


class WordSpider(scrapy.Spider):
    name = "word"
    allowed_domains = ["www.wordhippo.com"]
    start_urls = ["http://www.wordhippo.com/"]

    def parse(self, response):
        print(response.url)
