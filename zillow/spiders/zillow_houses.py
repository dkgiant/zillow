# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from ..utils import URL, cookie_parser
from ..items import ZillowItem
import json

class ZillowHousesSpider(scrapy.Spider):
    name = 'zillow_houses'
    allowed_domains = ['www.zillow.com']
    start_urls = [URL]
    
    def start_requests(self):
        yield scrapy.Request(
            url = URL,
            callback = self.parse,
            cookies=cookie_parser()
        )

    def parse(self, response):
        json_resp = json.loads(response.body)
        houses = json_resp.get('searchResults').get('listResults')
        for house in houses:
            loader = ItemLoader(item=ZillowItem())
            loader.add_value('id',house.get('id'))
            loader.add_value('img_src',house.get('imgSrc'))
            loader.add_value('detail_url',house.get('detailUrl'))
            loader.add_value('status_type',house.get('statusType'))
            loader.add_value('address',house.get('address'))
            loader.add_value('beds',house.get('beds'))
            loader.add_value('baths',house.get('baths'))
            loader.add_value('area_sqft',house.get('5010'))
            loader.add_value('latitude',house.get('latLong').get('latitude'))
            loader.add_value('longitude',house.get('latLong').get('longitude'))
            loader.add_value('broker_name',house.get('brokerName'))
            loader.add_value('broker_phone',house.get('brokerPhone'))
            yield loader.load_item()

