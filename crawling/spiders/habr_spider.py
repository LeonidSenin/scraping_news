import scrapy


class HabrSpiderSpider(scrapy.Spider):
    name = "habr_spider"
    allowed_domains = ["habr.com"]
    start_urls = ["https://habr.com/ru/articles/"]

    def parse(self, response):
        for link in response.css('h2.tm-title a::attr(href)'):
            yield response.follow(link, callback=self.parse_habr_news)

        for num_page in range(1,5):
            next_page = f'https://habr.com/ru/articles/page{num_page}/'
            yield response.follow(next_page, callback=self.parse)

    def parse_habr_news(self, response):
        yield {
            'title': response.css('h1.tm-title span::text').get(),
            'text': response.css('div.article-formatted-body p::text').getall(),
            }