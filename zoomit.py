# -*- coding: utf-8 -*-
import scrapy
from zoomit.items import zoomitItem

class ZoomitSpider(scrapy.Spider):
    name = 'zoomit'
    allowed_domains = ['zoomit.ir']
    start_urls = ['https://zoomit.ir']
    j=1
    def parse(self,response):
        for j in range(1,6):
            start_urls = ['https://zoomit.ir/tablet/page/'+str(j)]  
            print('url',start_urls)
            start_urls=str(start_urls[0])
            yield scrapy.Request(start_urls,callback=self.parse_main,encoding='utf-8')
            print('req',scrapy.Request(start_urls,callback=self.parse_main))
    def parse_main(self,response):
        links=response.xpath('//h3[@class="list_title_heading"]/a/@href').extract()             
        print('links:',links)
        i=1
        for link in links:            
            abs_url=response.urljoin(link)
            print('abs_url',abs_url)
            if (i<=len(links)):
                i=i+1
                yield scrapy.Request(abs_url,callback=self.parse_indential,encoding='utf-8')
                print('req**',scrapy.Request(abs_url,callback=self.parse_indential))
        return  
    def parse_indential(self, response):
        item=zoomitItem()
        item['date']= response.xpath('//div[@class="author-details-row2"]/span/text()').extract()
        item['writer_name']=response.xpath('//span[@itemprop="name"]/a//text()').extract()
        item['title']=response.xpath('//h1[@itemprop="headline"]/a/text()').extract()
        item['meta_categories']= response.xpath('//div[@class="catgroup"]/ul/li/a/text()').extract()
        item['abstract']= response.xpath('//div[@class="catgroup"]/ul/li/a/text()').extract()
        item['body_content']=response.xpath('//div[@id="bodyContainer"]/p//text()').extract()
        item['number_of_comments']= response.xpath('//div[@class="pad15L comments-header-title"]/span[@class="total-count"]//text()').extract()  
        item['number_of_comments']= response.xpath('//div[@class="z-comment-block"]/span[@class="z-comment-count"]/a[@class="z-comment-count-bubble"]/text()').extract()  
        item['coments_writer']=response.xpath('//li[@class="comment"]//div[@class="comment-wrapper"]//div[@class="comment-inner"]//div[@class="comment-details"]//div[@class="comment-meta"]//a//text()').extract()
        item['coments_body']=response.xpath('//li[@class="comment"]/text()').extract()
        return item
    
