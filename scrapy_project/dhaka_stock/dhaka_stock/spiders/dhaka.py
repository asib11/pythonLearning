import scrapy
from scrapy_splash import SplashRequest

class QuoteJsSpider(scrapy.Spider):
    name = "quote_js"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/js"]

    script = '''
        function main(splash, args)
            assert(splash:go(args.url))
            assert(splash:wait(0.5))
            splash: set_viewport_full()
            return{ html = splash:html()}
            
        end '''

    def start_requests(self):
        yield SplashRequest(url ="https://www.dsebd.org/latest_share_price_scroll_by_ltp.php", callback = self.parse, endpoint = 'execute', args = {'lua_source': self.script})
    def parse(self, response):
        products = response.xpath('//div[@class="table-responsive inner-scroll"]/table[@class="table table-bordered background-white shares-table fixedHeader"]/tbody')
        for product in products:
            yield {
                "TRADING CODE": f"https://www.dsebd.org/{product.xpath('.//tr/td[2]/a/@href').get()}",
                "TRADING CODE url": product.xpath('normalize-space(.//tr/td[2]/a/text())').get(),
                "LTP*": product.xpath('normalize-space(.//tr/td[3]/text())').get(),
                "HIGH": product.xpath('normalize-space(.//tr/td[4]/text())').get(),
                "LOW": product.xpath('normalize-space(.//tr/td[5]/text())').get(),
                "CLOSEP*": product.xpath('normalize-space(.//tr/td[6]/text())').get(),
                "YCP*": product.xpath('normalize-space(.//tr/td[7]/text())').get(),
                "CHANGE": product.xpath('normalize-space(.//tr/td[8]/text())').get(),
                "TRADE": product.xpath('normalize-space(.//tr/td[9]/text())').get(),
                "VALUE (mn)": product.xpath('normalize-space(.//tr/td[10]/text())').get(),
                "VOLUME": product.xpath('normalize-space(.//tr/td[11]/text())').get(),
            }