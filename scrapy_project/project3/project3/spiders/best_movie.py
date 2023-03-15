# import scrapy
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule


# class BestMovieSpider(CrawlSpider):
#     name = "best_movie"
#     allowed_domains = ["www.imdb.com"]
#     #start_urls = ["https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc"]

#     user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'

#     def start_requests(self):
#         yield scrapy.Request(url ="https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating", headers ={'User-Agent':self.user_agent})

#     rules = (Rule(LinkExtractor(restrict_xpaths= '//h3[@class="lister-item-header"]/a'), callback="parse_item", follow=True, process_request = 'set_user_agent'),)

#     def set_user_agent(self, request):
#         request.headers['User-Agent'] =self.user_agent
#         return request

#     def parse_item(self, response):
#         yield {
#             'title': response.xpath('//div[@class="sc-b5e8e7ce-1 kNhUtn"]/h1[@class="sc-b73cd867-0 gLtJub"]/text()').get()
#         }

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMovieSpider(CrawlSpider):
    name = "best_movie"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating"]
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }

    rules = (Rule(LinkExtractor(restrict_xpaths= '//h3[@class="lister-item-header"]/a'), callback="parse_item", follow=True),)

    def parse_item(self, response):
            yield {
                'title': response.xpath('//div[@class="sc-b5e8e7ce-1 kNhUtn"]/h1[@class="sc-b73cd867-0 gLtJub"]/text()').get()
            }
