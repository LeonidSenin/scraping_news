import scrapy


class DevGangNewsSpider(scrapy.Spider):
    name = "dev_gang_news"
    allowed_domains = ["dev-gang.ru"]
    start_urls = ["https://dev-gang.ru"]

    def parse(self, response):
        for link in response.css('h3.home__article-name a::attr(href)'):
            yield response.follow(link, callback=self.parse_dev_gang_news)

        for num_page in range(1, 5):
            next_page = f'https://dev-gang.ru/?page={num_page}'
            yield response.follow(next_page, callback=self.parse)

    def parse_dev_gang_news(self, response):
        yield {
            'title':  response.css('h1.article__name::text').get(),
            'text': response.css('div.article__content p::text').getall(),
            # 'page_num': response.css('a.pagination__item::text').get().strip()
            }
