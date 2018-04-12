# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UkPipelineItem(scrapy.Item):
    # define the fields for your item here like:
    uk_anis = scrapy.Field()


class DePipelineItem(scrapy.Item):
    de_anis = scrapy.Field()
