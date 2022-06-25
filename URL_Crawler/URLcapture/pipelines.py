# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.exporters import CsvItemExporter
import pymongo
import os
class CsvPipeline:
    collection = 'links'

    @classmethod 
    def from_crawler(cls, crawler): 
        output = os.path.abspath("./output") + '/urls/' + str(crawler.settings.get('output'))
        mongodb_uri = crawler.settings.get('MONGODB_URI'),
        mongodb_db = crawler.settings.get('MONGODB_DATABASE', 'items')
        layer = crawler.settings.get('layer')
        return cls(output, mongodb_uri, mongodb_db, layer) 

    def __init__(self, output, mongodb_url, mongodb_db, layer):
        # Open files
        self.file = open(output, 'wb')
        self.exporter = CsvItemExporter(self.file, encoding='big5')
        self.exporter.start_exporting()
        
        self.mongodb_uri = mongodb_url
        self.mongodb_db = mongodb_db
        self.layer = layer

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongodb_uri)
        self.db = self.client[self.mongodb_db]
        # self.db[self.collection].delete_many({})      # Clear the content of collections

    def process_item(self, item, spider):
        result = self.db[self.collection].find_one({
            "urls" : { "$eq" : item["urls"] }
        })

        # If crawler capture the same url, drop it
        if result == None:
            item['layer'] = self.layer 
            self.exporter.export_item(item)
            data = dict(item)
            self.db[self.collection].insert_one(data)
            return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
        self.client.close()