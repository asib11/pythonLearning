import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMovieSpider(CrawlSpider):
    name = "book"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }

    rules = (Rule(LinkExtractor(restrict_xpaths= '//h3/a'), callback="parse_item", follow=True),Rule(LinkExtractor(restrict_xpaths ='//li[@class="next"]/a')))


    def parse_item(self, response):

        yield {
            'book name': response.xpath('//div[@class="col-sm-6 product_main"]/h1/text()').get(),
            'book url': response.url,
            'book price': response.xpath('(//div[@class="col-sm-6 product_main"]/p)[1]/text()').get(),
            'book stock': response.xpath('normalize-space((//div[@class="col-sm-6 product_main"]/p[@class="instock availability"]/text())[2])').get()
        }
