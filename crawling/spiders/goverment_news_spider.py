import scrapy


class GovermentNewsSpiderSpider(scrapy.Spider):
    name = "goverment_news_spider"
    allowed_domains = ["government.ru"]
    start_urls = ["http://government.ru/news/"]

    def parse(self, response):
        for link in response.css('a.headline__link::attr(href)'):
            yield response.follow(link, callback=self.parse_gov)
    def parse_gov(self,response):
        yield {
            'title': response.css('h3.reader_article_headline::text').get().strip()
        }