import scrapy
from AmazonScrapy.items import DePipelineItem


class UkAmazonSpider(scrapy.Spider):
    name = 'deamazonspider'
    # allowed_domains = ["amazon"]
    start_urls = [
        'https://www.amazon.de/s?marketplaceID=A1PA6795UKMFR9&me=ANZYLS5IXG3VI&merchant=ANZYLS5IXG3VI&redirect=true']

    def parse(self, response):
        anis_list = response.xpath("//li/div[@class='s-item-container']")
        for anis in anis_list:
            item = DePipelineItem()
            anis_link = anis.xpath("./div[3]/div[1]/a/@href").extract()[0]
            item["de_anis"] = anis_link.split('/dp/')[1].split('/')[0]
            if len(anis.xpath(".//div[@class='a-box-inner a-padding-mini']")) > 0:
                print('more')
                yield scrapy.Request(anis_link, callback=self.parse_more)

            yield item
        if len(response.xpath("//a[@id='pagnNextLink']")) > 0:
            next_url = response.xpath("//a[@id='pagnNextLink']/@href").extract()[0]
            print(next_url)
            yield scrapy.Request("https://www.amazon.de" + next_url, callback=self.parse)

    @classmethod
    def parse_more(self, response):
        # 拿更多的
        data_asin = response.xpath("//div[@id='variation_color_name']/ul/li")
        if data_asin is None:
            return
        for data in data_asin:
            item = DePipelineItem()
            dataa = data.xpath("./@data-defaultasin").extract()[0]
            item["de_anis"] = dataa + "-more"
            yield item
