# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from scrapy.pipelines.images import ImagesPipeline

# class ResearchPipeline:
#     def process_item(self, item, spider):
#         return item

class CustomImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for file_url in item['image_urls']:
            yield scrapy.Request(file_url)