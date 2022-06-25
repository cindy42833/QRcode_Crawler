import scrapy
from research.items import ImageItem

class ExampleSpider(scrapy.Spider):
    name = 'example'

    with open('first_cat1.csv') as file:
        start_urls = [line.strip() for line in file]

    def parse(self, response):
        item = ImageItem()
        if response.status == 200:
            rel_img_urls = response.xpath("//img/@src").getall()
            # item['image_urls'] = self.url_join(rel_img_urls, response)
            item['image_urls'] = rel_img_urls
            print(item)
        return item

    def url_join(self, rel_img_urls, response):
        joined_urls = []
        for rel_img_url in rel_img_urls:
            joined_urls.append(response.urljoin(rel_img_url))

        return joined_urls
