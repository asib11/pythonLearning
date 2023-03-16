import scrapy
from scrapy_splash import SplashRequest

class QuoteJsSpider(scrapy.Spider):
    name = "quote_js"
    allowed_domains = ["quotes.toscrape.com"]
    script = '''
        function main(splash, args)
            assert(splash:go(args.url))
            assert(splash:wait(0.5))
            splash: set_viewport_full()
            return splash:html()
            
        end '''

    def start_requests(self):
        yield SplashRequest(url ="http://quotes.toscrape.com/js", callback = self.parse, endpoint = 'execute', args = {'lua_source': self.script})
    
    def parse(self, response):
        products = response.xpath('//div[@class = "quote"]')
        for product in products:
            yield {
                "QUOTE": product.xpath('.//span[@class="text"]/text()').get(),
                "AUTHOR": product.xpath('.//span/small[@class="author"]/text()').get(),
                'TAG': product.xpath('.//div[@class="tags"]/a/text()').getall()
            }

        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page:
            yield SplashRequest(
                url=f"http://quotes.toscrape.com{next_page}",
                callback=self.parse,
                endpoint = 'execute',
                args = {'lua_source': self.script}
            )