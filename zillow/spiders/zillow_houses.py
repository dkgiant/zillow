# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from ..utils import URL, cookie_parser,parse_new_url
from ..items import ZillowItem
import json

class ZillowHousesSpider(scrapy.Spider):
    name = 'zillow_houses'
    allowed_domains = ['www.zillow.com']
    
    
    def start_requests(self):
        yield scrapy.Request(
            url = URL,
            callback = self.parse,
            cookies=cookie_parser(),
            meta={
                'current_page':1
            }
        )

    def parse(self, response):
        current_page = response.meta['current_page']
        json_resp = json.loads(response.body)
        houses = json_resp.get('searchResults').get('listResults')
        for house in houses:
            loader = ItemLoader(item=ZillowItem())
            loader.add_value('id',house.get('id'))
            loader.add_value('image_urls',house.get('imgSrc'))
            loader.add_value('detail_url',house.get('detailUrl'))
            loader.add_value('status_type',house.get('statusType'))
            loader.add_value('address',house.get('address'))
            loader.add_value('beds',house.get('beds'))
            loader.add_value('baths',house.get('baths'))
            loader.add_value('area_sqft',house.get('area'))
            loader.add_value('latitude',house.get('latLong').get('latitude'))
            loader.add_value('longitude',house.get('latLong').get('longitude'))
            loader.add_value('broker_name',house.get('brokerName'))
            loader.add_value('broker_phone',house.get('brokerPhone'))
            yield loader.load_item()
        
        total_pages = json_resp.get('searchList').get('totalPages')
        if current_page <= total_pages:
            next_page = current_page+1
            yield scrapy.Request(
                url = parse_new_url(URL,page_number=next_page),
                callback = self.parse,
                cookies=cookie_parser(),
                meta={
                    'current_page':next_page
                }
            )
