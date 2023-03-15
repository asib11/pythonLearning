import scrapy


class MultipageSpider(scrapy.Spider):
    name = "multipage"
    allowed_domains = ["www.glassesshop.com"]
    # start_urls = ["https://www.glassesshop.com/bestsellers"] when use request spoofing, no need to use this url

    def start_requests(self):
        yield scrapy.Request(
            url="https://www.glassesshop.com/bestsellers",
            callback=self.parse,
            headers={
                "User-Agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
            },
        )

    def parse(self, response):
        products = response.xpath(
            '//div[@class="row pt-lg-5 product-list column-1"]/div[@class="col-12 pb-5 mb-lg-3 col-lg-4 product-list-row text-center product-list-item"]'
        )
        # products = response.xpath('//div[@class="row pt-lg-5 product-list column-1"]/div')
        for product in products:
            yield {
                "product url": product.xpath(
                    './/div[@class="p-title-block"]/div[@class="mt-3"]/div[@class="row no-gutters"]/div[1]/div/a[1]/@href'
                ).get(),
                "image url": product.xpath(
                    './/div[@class="product-img-outer"]/a[1]/img[1]/@data-src'
                ).get(),
                "product name": product.xpath(
                    'normalize-space(.//div[@class="p-title-block"]/div[@class="mt-3"]/div[@class="row no-gutters"]/div[1]/div/a[1]/text())'
                ).get(),
                "product price": product.xpath(
                    './/div[@class="p-title-block"]/div[@class="mt-3"]/div[@class="row no-gutters"]/div[2]/div/div[2]/span/text()'
                ).get(),
                "user agent": response.request.headers["User-Agent"],
            }
        next_page = response.xpath('//a[@class="page-link"]/@href').get()
        if next_page:
            yield scrapy.Request(
                url=next_page,
                callback=self.parse,
                headers={
                    "User-Agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
                },
            )
