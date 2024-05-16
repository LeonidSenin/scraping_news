## Инструкция 

1. Устанавливаем фреймворк Scrapy командой - pip install scrapy
2. Создаем Scrapy проект с именем _crawling_ командой - scrapy startproject crawling
3. Переходим в папку _crawling_ с помощью команды - cd crawling
4. В папке _crawling_ нашего проекта находятся файлы:
    - items.py содержит классы, которые перечисляют поля собираемых данных,
    - pipelines.py позволяет задать определенные действия при открытии/закрытии паука, сохранения данных,
    - settings.py содержит пользовательские настройки паука,
    - spiders — папка, в которой хранятся файлы с классами пауков. Каждого паука принято писать в отдельном файле с именем name_spider.py.
5. В папке _spiders_ создаем нового паука командой - scrapy genspider goverment_news_spider government.ru, где
   - goverment_news_spider - имя py файла
   - government.ru - домен сайта

```python
import scrapy


class GovermentNewsSpiderSpider(scrapy.Spider):
    name = "goverment_news_spider"
    allowed_domains = ["government.ru"]
    start_urls = ["http://government.ru/news/"]
```

    - name — имя паука, используется для запуска,
    - allowed_domains — домены сайта, за пределами которого пауку искать ничего не следует,
    - start_urls — список начальных адресов,
    - rules — список правил для извлечения ссылок
6. Далее прописать команду в терминале _scrapy shell_ , таким образом откроется консоль для отладки внутри терминала 
7. После этого через команду fetch можм обратится к сайту, с которым будем работать командой - fetch('http://government.ru/news/')
8. В ответ получаем сообщение, что сайт работает и отдает нам информацию 2024-05-14 11:27:41 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://government.ru/news/> (referer: None)
9. Далее командой обращаемся к сайту через response через css response.css('a.headline__link::attr(href)') в данной команде мы ищем тег _а_ с именем класса _headline__link_ и забираем _href_
10. Выходим из _scrapy shell_ командой exit()
11. Напишем код:
В функции parse с помощью цикла проходим по всем ссылкам в заданном теге с помощью функции callback открываем ссылку и далее в функции parse_gov возвращаем заголовок каждой новости 
for link in response.css('a.headline__link::attr(href)'):
    yield response.follow(link, callback=self.parse_gov)
```python
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
```


