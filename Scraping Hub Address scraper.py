import scrapy

class ContactSpider(scrapy.Spider):
    name = 'contactspider'
    start_urls = ['https://scrapinghub.com/']
 
    def parse(self,response):
        all_info = response.css("div.company-info")  
        yield {
            'building': all_info.css("p::text").get(), 
            'street': all_info.css("p::text").getall()[1],
            'city_and_country': all_info.css("p::text").getall()[2]
        }