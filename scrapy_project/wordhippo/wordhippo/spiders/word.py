import scrapy


class WordSpider(scrapy.Spider):
    name = "word"
    allowed_domains = ["www.wordhippo.com"]
    start_urls = ["http://www.wordhippo.com/"]
    def start_requests(self):
        yield scrapy.Request(
            url=f"https://www.wordhippo.com/what-is/another-word-for/community.html",
            callback=self.parse,
            headers={
                "User-Agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
            },
        )

    def parse(self, response):
        # for product in response.xpath('//div[@class="wordtype"]'):
        #     yield {
        #         "word type": product.xpath('normalize-space(./text())').get(),
        #         #"defination":product.xpath('normalize-space(//div[@class="tabdesc"]/text())').get(),
        #         "word": [p.xpath("./div[@class='wb']/a/text()").get() for p in product.xpath("//div[@class='relatedwords']")],
        #     }
        # for product2 in response.xpath('//div[@class="tabdesc"]'):
        #     yield {
        #         "defination":product2.xpath('normalize-space(./text())').get()
        #     }
        wordtype = [ product.xpath('normalize-space(.//text())').get() for product in response.xpath('//div[@class="wordtype"]')]
        word = [[q.xpath(".//a/text()").get() for q in p.xpath(".//div[@class='wb']")] for p in response.xpath("//div[@class='relatedwords']") ]
        defination= [product2.xpath('normalize-space(.//text())').get() for product2 in response.xpath('//div[@class="tabdesc"]')]

        yield {
            'wordtype': wordtype,
            'word': word,
            'defination': defination
        }
                
            

        # next_page = response.xpath('//a[@class="page-link"]/@href').get()
        # if next_page:
        #     yield scrapy.Request(
        #         url=next_page,
        #         callback=self.parse,
        #         headers={
        #             "User-Agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
        #         },
            
