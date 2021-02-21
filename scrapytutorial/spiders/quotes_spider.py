import scrapy

class QuotesSpider(scrapy.Spider):
    name = "propertypro"
    start_urls = [
        'https://www.propertypro.ng/property-for-rent?search=&type=&bedroom=&min_price=&max_price='
    ]   
    
    def parse(self, response):
        for quote in response.css('div.single-room-text'):
            yield {
                'Title': quote.css('.listings-property-title::text').get(),
                'Address': quote.css('h4::text').get(),
                'Description': quote.css('h3.listings-property-title2::text').get(),
                'Price': quote.css('.listings-price span::text').getall(),
            }

        for a in response.css('li.page-item a'):
            yield response.follow(a, callback=self.parse)

        