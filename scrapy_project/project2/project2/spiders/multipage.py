import scrapy


class MultipageSpider(scrapy.Spider):
    name = "multipage"
    allowed_domains = ["www.glassesshop.com"]
    start_urls = ["https://www.glassesshop.com/bestsellers"]

    def parse(self, response):
        products = response.xpath('//div[@class="row pt-lg-5 product-list column-1"]/div[@class="col-12 pb-5 mb-lg-3 col-lg-4 product-list-row text-center product-list-item"]')
        for product in products:
            yield{
                'product url': product.xpath('(.//div[@class="product-img-outer"]/a/@href)').get(),
                'image url': product.xpath('.//div[@class="product-img-outer"]/a/img[1]/@data-src').get(),
                'product name': product.xpath('.//div[@class="p-title-block"]/div[@class="mt-3"]/div[@class="row no-gutters"]/div[1]/div/a/text()').get(),
                'product price': product.xpath('.//div[@class="p-title-block"]/div[@class="mt-3"]/div[@class="row no-gutters"]/div[2]/div/div[2]/span/text()').get()
            }
