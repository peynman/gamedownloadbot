from pathlib import Path
import scrapy


class FitGirlSpider(scrapy.Spider):
    name = "fitgirl"

    def start_requests(self):
        urls = [
            'https://fitgirl-repacks.site/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for content in response.css('.entry-content'):
            item = {}
            item['title'] = content.css('h3 strong').css('::text').get()
            if item['title'] == 'Upcoming repacks': continue
            item['images'] = content.css('p a img::attr(src)').extract()
            item['metas'] = []
            for meta in content.css('p strong'):
                item['metas'].append(meta.css('::text').get())
            if len(item['metas']) == 5:
                item['tags'] = [x.strip() for x in item['metas'][0].split(',')]
                item['company'] = [x.strip() for x in item['metas'][1].split(',')]
                item['lang'] = [x.strip() for x in item['metas'][2].split(',')]
                item['originalSize'] = item['metas'][3]
                item['downloadSize'] = item['metas'][4]
            yield item
        next_page = response.css('a.next.page-numbers::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)