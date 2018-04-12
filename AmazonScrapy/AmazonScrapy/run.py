from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess


# 执行多个爬虫
class Runner(object):
    @classmethod
    def run(self):
        setting = get_project_settings()
        process = CrawlerProcess(setting)
        didntWorkSpider = []

        for spider_name in process.spiders.list():
            if spider_name in didntWorkSpider:
                continue
            print("Running spider %s" % (spider_name))
            process.crawl(spider_name)
        process.start()


if __name__ == '__main__':
    Runner().run()
