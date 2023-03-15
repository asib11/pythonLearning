# import scrapy


# class CountriesSpider(scrapy.Spider):
#     name = "countries"
#     allowed_domains = ["www.worldometers.info"]
#     start_urls = ["https://www.worldometers.info/world-population/population-by-country/"]

#     def parse(self, response):
#         # title = response.xpath('//h1/text()').get()
#         countries = response.xpath('//td/a')
#         for name in countries:
#             countries_name = name.xpath('.//text()').get()
#             link = name.xpath('.//@href').get()
#             # yield {'countires name': countries_name, 'countries link': link}
#             # absolute_url = f'https://www.worldometers.info{linffk}' #method 1
#             # absolute_url = response.urljoin(link) #method 2
#             # yield scrapy.Request(url = absolute_url)
#             yield response.follow(url = link, callback = self.country_parser, meta = {'countries name':countries_name})

#     def country_parser(self, response):
#         rows = response.xpath('(//table[@class="table table-striped table-bordered table-hover table-condensed table-list"])[1]/tbody/tr')
#         for row in rows:
#             name = response.request.meta['countries name']
#             year = row.xpath('.//td[1]/text()').get()
#             population = row.xpath('.//td[2]/strong/text()').get()
#             yield {'country':name,'year': year, 'population': population}


import scrapy 
 
 
class GdpSpider(scrapy.Spider): 
    name = "countries" 
    allowed_domains = ["www.worldpopulationreview.com"] 
    start_urls = [ 
        "https://worldpopulationreview.com/country-rankings/countries-by-national-debt"] 
 
    def parse(self, response): 
        rows = response.xpath("//tbody[@class = 'jsx-a3119e4553b2cac7']") 
        for row in rows: 
            country = row.xpath(".//tr/td[1]/a/text()").get() 
            debt = row.xpath(".//tr/td[4]/text()").get() 
 
            yield { 
                'country': country, 
                'debt': debt 
            }