import scrapy

from scrapy.item import Item,Field

class zoomitItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #defining our item fields
    title=scrapy.Field()
    meta_categories=scrapy.Field()
    body_content=scrapy.Field()
    coments_title=scrapy.Field()
    coments_body=scrapy.Field()
    writers=scrapy.Field()
    stars=scrapy.Field()
    abstract=scrapy.Field()
    number_of_comments=scrapy.Field()
    date=scrapy.Field()
    writer_name=scrapy.Field()
    coments_writer=scrapy.Field()
    
    #popularity=scrapy.Field()
    #year=scrapy.Field()
    #ratingCount=scrapy.Field()