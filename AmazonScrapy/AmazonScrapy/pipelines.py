# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from AmazonScrapy.items import UkPipelineItem, DePipelineItem


class AmazonscrapyPipeline(object):
    def __init__(self):
        self.uk_file = open("txt/uk_amaozninfo.txt", "w")
        self.de_file = open("txt/de_amaozninfo.txt", "w")

    def process_item(self, item, spider):
        if isinstance(item, UkPipelineItem):
            self.uk_file.write(item["uk_anis"] + "\n")
        if isinstance(item, DePipelineItem):
            self.de_file.write(item["de_anis"] + "\n")
        return item

    def close_spider(self, spider):
        self.uk_file.close()
        self.de_file.close()

